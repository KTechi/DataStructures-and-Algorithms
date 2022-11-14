public class Elgamal {
	private final long P;//  prime = public key
	private final long G;//  random(1 to P-1) = public key
	private final long X;//  random(0 to P-2) = secret key
	private final long Y;//  G^X (modulo P) = public key
	private final long M;//  message -> C1^{P-1-X} * C2 (modulo P)
	private final long C1;// G^R (modulo P) = enc
	private final long C2;// M * Y^R (modulo P) = enc

	Elgamal() {
		this(160481183, 123456789L);
	}
	Elgamal(long m) {
		this(160481183, m);
	}
	Elgamal(long p, long m) {
		long stop, start = System.currentTimeMillis();

		this.P = p;
		this.G = (long)(Math.random() * (P - 1) + 1);
		this.X = (long)(Math.random() * (P - 1));
		this.Y = powMod(G, X);
		this.M = m;
		long r = (long)(Math.random() * (P - 1));
		this.C1 = powMod(G, r);
		this.C2 = powMod(Y, r) * M % P;

		System.out.println("Decode = " + C2 * powMod(C1, P - 1 - X) % P);
		stop = System.currentTimeMillis();
		System.out.println((stop - start) / 1000.0 + "[sec]");
	}

	void printElgamal() {
		System.out.println("P  = " + this.P);
		System.out.println("G  = " + this.G);
		System.out.println("Y  = " + this.Y);
		System.out.println("X  = " + this.X);
		System.out.println("C1 = " + this.C1);
		System.out.println("C2 = " + this.C2);
		System.out.println();
	}

	private long powMod(long x, long y) {
		if (y == 0) return 1;
		return (y % 2 == 0) ? powMod(x * x % P, y / 2) : x * powMod(x, y - 1) % P;
	}
}
