public class Main {
	public static void main(String[] args) {
		RSA r = new RSA(Long.parseLong(args[0]));
		Elgamal e = new Elgamal(Long.parseLong(args[0]));
		r.printRSA();
		e.printElgamal();
	}
}
