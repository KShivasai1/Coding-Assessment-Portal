public class Addition {
public static void main(String args[]) {
	Addition a  = new Addition();
	a.addition(80,90);
}
public int addition(int a, int b) {
	int total = a + b;
	System.out.println("Total value: "+total);
	return total;
}
}
