from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
			path("AdminLogin.html", views.AdminLogin, name="AdminLogin"),
			path("AdminLoginAction", views.AdminLoginAction, name="AdminLoginAction"),
			path("Signup.html", views.Signup, name="Signup"),
			path("SignupAction", views.SignupAction, name="SignupAction"),	    	
			path("UserLogin.html", views.UserLogin, name="UserLogin"),
			path("UserLoginAction", views.UserLoginAction, name="UserLoginAction"),
			path("ViewUsers", views.ViewUsers, name="ViewUsers"),
			path("PythonAssessment", views.PythonAssessment, name="PythonAssessment"),
			path("JavaAssessment", views.JavaAssessment, name="JavaAssessment"),
			path("CompilePython", views.CompilePython, name="CompilePython"),
			path("CompileJava", views.CompileJava, name="CompileJava"),
			path("AddChallenges.html", views.AddChallenges, name="AddChallenges"),
			path("AddChallengesAction", views.AddChallengesAction, name="AddChallengesAction"),
			path("ViewAdminChallenge.html", views.ViewAdminChallenge, name="ViewAdminChallenge"),
			path("AcceptChallenge", views.AcceptChallenge, name="AcceptChallenge"),
			path("AcceptChallengeAction", views.AcceptChallengeAction, name="AcceptChallengeAction"),
			path("ViewChallenges", views.ViewChallenges, name="ViewChallenges"),
			path("ChallengeScore", views.ChallengeScore, name="ChallengeScore"),
			path("ChallengeScoreAction", views.ChallengeScoreAction, name="ChallengeScoreAction"),
]