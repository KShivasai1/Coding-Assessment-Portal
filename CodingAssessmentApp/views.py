from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
import os
import pymysql
import subprocess
from django.http import HttpResponse
from datetime import date

global uname

def JavaAssessment(request):
    if request.method == 'GET':
        return render(request, 'JavaAssessment.html', {})


def PythonAssessment(request):
    if request.method == 'GET':
        return render(request, 'PythonAssessment.html', {})

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def AdminLogin(request):
    if request.method == 'GET':
       return render(request, 'AdminLogin.html', {})

def UserLogin(request):
    if request.method == 'GET':
       return render(request, 'UserLogin.html', {})    

def Signup(request):
    if request.method == 'GET':
       return render(request, 'Signup.html', {})

def AddChallenges(request):
    if request.method == 'GET':
       return render(request, 'AddChallenges.html', {})    

def CompileJava(request):
    if request.method == 'GET':
        code = request.GET.get('mytext', False)
        code = code.replace("@","\n")
        codes = code.split("\n")
        cname = ""
        for i in range(len(codes)):
            temp = codes[i].split(" ")
            if len(temp) >= 2:
                if temp[0].strip() == 'class' or temp[1].strip() == 'class':
                    if temp[0].strip() == 'class':
                        cname = temp[1].strip()
                    if temp[1].strip() == 'class':
                        cname = temp[2].strip()
        print(cname)                
        f = open(cname+".java", "w")
        f.write(code)
        f.close()
        calljava = subprocess.Popen(["javac",cname+".java"], stderr=subprocess.PIPE)
        compiled = calljava.stderr.read()
        compile_errors = compiled.decode().strip()
        length = len(compile_errors)
        print("lenght : "+str(length))
        output = ""
        if length == 0:
            output += "Compilation Detail: compiled successfully\n"
            calljava = subprocess.Popen(["java",cname, "10","20"], stdout=subprocess.PIPE)
            compiled = calljava.stdout.read()
            output += "Execution Detail "+compiled.decode()+"\nYour Coding Grade: 100%"
        else:
            arr = compile_errors.split("\n")
            errors = arr[len(arr)-1]
            err = errors.split(" ")
            err = int(err[0])
            grade = err / len(codes)
            output += compile_errors+"\n\nYour Coding Grade: "+str(grade)
        if os.path.exists(cname+".java"):
            os.remove(cname+".java")
        if os.path.exists(cname+".class"):
            os.remove(cname+".class")     
        return HttpResponse(output, content_type="text/plain")      

def CompilePython(request):
    if request.method == 'GET':
        code = request.GET.get('mytext', False)
        code = code.replace("@","\n")
        codes = code.split("\n")
        print(code)
        f = open("test.py", "w")
        f.write(code)
        f.close()
        callpython = subprocess.Popen(["python","test.py", "40","20"], stderr=subprocess.PIPE)
        error = callpython.stderr.read()
        error = error.decode()
        output = error
        if len(error) == 0:
            callpython = subprocess.Popen(["python","test.py", "40","20"], stdout=subprocess.PIPE)
            output = callpython.stdout.read()
            output = output.decode()+"\n\nCode Compilation Successfull, Your Coding Grade = 100%"
            #print("Execution Detail "+output)            
        else:
            arr = len(error.split("\n")) / 2
            grade = len(codes) / arr
            output = "Errors occured: "+error+"\n\nYour Coding grade: "+str(grade)
        return HttpResponse(output, content_type="text/plain")            

def AdminLoginAction(request):
    global uname
    if request.method == 'POST':
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        if username == 'admin' and password == 'admin':
            uname = username
            context= {'data':'welcome '+uname}
            return render(request, 'AdminScreen.html', context)
        else:
            context= {'data':'invalid login details'}
            return render(request, 'AdminLogin.html', context)
    

def AcceptChallenge(request):
    if request.method == 'GET':
        global uname
        cid = request.GET.get('t1', False)
        output = '<td><input type="text" name="t1" style="font-family: Comic Sans MS" size="30" value="'+str(cid)+'" readonly></td></tr>'
        context= {'data1':output}
        return render(request, 'AcceptChallenge.html', context)
        

def getScore(sname,cid):
    score = 'none'
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Assessment',charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute("select * from challenge_result")
        rows = cur.fetchall()
        for row in rows:
            if row[0] == cid and row[1] == sname:
                score = row[3]
                break
    return score                

def ViewAdminChallenge(request):
    if request.method == 'GET':
        global uname
        output = ""
        font = '<font size="" color="black">'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Assessment',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * from challenges")
            rows = cur.fetchall()
            for row in rows:
                output += '<tr><td>'+font+str(row[0])+'</td>'
                output += '<td>'+font+row[1]+'</td>'
                output += '<td>'+font+str(row[2])+'</td>'
                score = getScore(uname,row[0])
                if score == 'none':
                    output+='<td><a href=\'AcceptChallenge?t1='+str(row[0])+'\'><font size=3 color=black>Click Here to Answer</font></a></td></tr>'
                else:
                    output += '<td>'+font+'Already Submitted. Your Score: '+score+'</td>'
        context= {'data':output}
        return render(request, 'ViewAdminChallenge.html', context)   

def ViewUsers(request):
    if request.method == 'GET':
        global uname
        output = ""
        font = '<font size="" color="black">'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Assessment',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * from signup")
            rows = cur.fetchall()
            for row in rows:
                output += '<tr><td>'+font+str(row[0])+'</td>'
                output += '<td>'+font+row[1]+'</td>'
                output += '<td>'+font+row[2]+'</td>'
                output += '<td>'+font+row[3]+'</td>'
                output += '<td>'+font+row[4]+'</td>'                             
        context= {'data':output}
        return render(request, 'ViewUsers.html', context)    

def UserLoginAction(request):
    global uname
    if request.method == 'POST':
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        usertype = request.POST.get('t3', False)
        index = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Assessment',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username,password FROM signup")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and password == row[1]:
                    uname = username
                    index = 1
                    break
        page = "UserLogin.html"        
        if index == 1:
            page = "UserScreen.html"
        if page != "UserLogin.html":
            context= {'data':'welcome '+uname}
            return render(request, page, context)
        else:
            context= {'data':'invalid login details'}
            return render(request, page, context)

def SignupAction(request):
    if request.method == 'POST':
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        contact = request.POST.get('t3', False)
        email = request.POST.get('t4', False)
        address = request.POST.get('t5', False)        
        output = "none"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Assessment',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username FROM signup")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username:
                    output = username+" Username already exists"
                    break
        if output == 'none':
            db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Assessment',charset='utf8')
            db_cursor = db_connection.cursor()
            student_sql_query = "INSERT INTO signup(username,password,contact_no,email,address) VALUES('"+username+"','"+password+"','"+contact+"','"+email+"','"+address+"')"
            db_cursor.execute(student_sql_query)
            db_connection.commit()
            print(db_cursor.rowcount, "Record Inserted")
            if db_cursor.rowcount == 1:
                output = 'Signup Process Completed'
        context= {'data':output}
        return render(request, 'Signup.html', context)


def AddChallengesAction(request):
    if request.method == 'POST':
        challenge = request.POST.get('t1', False)
        today = date.today()
        count = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Assessment',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select count(*) FROM challenges")
            rows = cur.fetchall()
            for row in rows:
                count = row[0]
        count = count + 1
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Assessment',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO challenges(challenge_id,challenge_data,challenge_date) VALUES('"+str(count)+"','"+challenge+"','"+str(today)+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            output = 'Challenge details added with ID: '+str(count)
        context= {'data':output}
        return render(request, 'AddChallenges.html', context)

def AcceptChallengeAction(request):
    if request.method == 'POST':
        global uname
        cid = request.POST.get('t1', False)
        answer = request.POST.get('t2', False)
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Assessment',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO challenge_result(challenge_id,student_name,student_answer,score) VALUES('"+cid+"','"+uname+"','"+answer+"','Pending')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            output = 'Your answer accepted'
        context= {'data':output}
        return render(request, 'UserScreen.html', context)        



def ViewChallenges(request):
    if request.method == 'GET':
        global uname
        output = ""
        font = '<font size="" color="black">'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Assessment',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * from challenge_result where score='Pending'")
            rows = cur.fetchall()
            for row in rows:
                output += '<tr><td>'+font+str(row[0])+'</td>'
                output += '<td>'+font+row[1]+'</td>'
                output += '<td>'+font+row[2]+'</td>'
                output+='<td><a href=\'ChallengeScore?t1='+str(row[0])+'&t2='+row[1]+'\'><font size=3 color=black>Click Here to Give Score</font></a></td></tr>'
        context= {'data':output}
        return render(request, 'ViewChallenges.html', context)   

def getAnswer(cid,sname):
    answer = "none"
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Assessment',charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute("select student_answer from challenge_result where challenge_id='"+str(cid)+"' and student_name='"+sname+"'")
        rows = cur.fetchall()
        for row in rows:
            answer = row[0]
            break
    return answer 

def ChallengeScore(request):
    if request.method == 'GET':
        cid = request.GET.get('t1', False)
        sname = request.GET.get('t2', False)
        answer = getAnswer(cid,sname)
        output = '<td><input type="text" name="t1" style="font-family: Comic Sans MS" size="30" value="'+cid+'" readonly></td></tr>'
        output+= '<tr><td><font size="" color="black">Student&nbsp;Name</b></td>'
        output += '<td><input type="text" name="t2" style="font-family: Comic Sans MS" size="30" value="'+sname+'" readonly></td></tr>'
        output+= '<tr><td><font size="" color="black">Student&nbsp;Answer</b></td>'
        output+= '<td><textarea name="t3" rows="15" cols="80">'+answer+'</textarea></td></tr>'
        context= {'data1':output}
        return render(request, 'ChallengeScore.html', context)

def ChallengeScoreAction(request):
    if request.method == 'POST':
        cid = request.POST.get('t1', False)
        sname = request.POST.get('t2', False)
        score = request.POST.get('t4', False)
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'Assessment',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "update challenge_result set score='"+score+"' where challenge_id='"+str(cid)+"' and student_name='"+sname+"'"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            output = 'Score successfully assigned to '+sname
        context= {'data':output}
        return render(request, 'AdminScreen.html', context)        


      
