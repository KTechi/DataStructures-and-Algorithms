public class RSA {
	private final long P;// prime = secret key
	private final long Q;// prime = secret key
	private final long N;// P * Q = public key
	private final long L;// L = least_common_multiple(P-1, Q-1) = secret key
	private final long E;// 1 = greatest_common_divisor(L, E) = public key
	private final long D;// 1 = E * D (modulo L) = secret key
	private final long M;// message -> C^D (modulo N)
	private final long C;// M^E (modulo N) = enc

	RSA() {
		this(55931L, 51673L, 1234567890L);
	}
	RSA(long m) {
		this(55931L, 51673L, m);
	}
	RSA(long p, long q, long m) {
		long stop, start = System.currentTimeMillis();

		this.P = p;
		this.Q = q;
		this.N = p * q;
		this.L = lcm(p - 1, q - 1);
		long e = 2L;
		while (gcd(L, e) != 1) e++;
		this.E = e;
		this.D = secretKeyGen(L, E);
		this.M = m;
		this.C = powMod(M, E);

		System.out.println("Decode = " + powMod(C, D));
		stop = System.currentTimeMillis();
		System.out.println((stop - start) / 1000.0 + "[sec]");
	}

	void printRSA() {
		System.out.println("P = " + this.P);
		System.out.println("Q = " + this.Q);
		System.out.println("N = " + this.N);
		System.out.println("L = " + this.L);
		System.out.println("E = " + this.E);
		System.out.println("D = " + this.D);
		System.out.println("M = " + this.M);
		System.out.println("C = " + this.C);
		System.out.println();
	}

	private long gcd(long x, long y) {
		return (y == 0) ? x : gcd(y, x % y);
	}

	private long lcm(long x, long y) {
		return x * y / gcd(x, y);
	}

	private long powMod(long x, long y) {
		if (y == 0) return 1;
		return (y % 2 == 0) ? powMod(x * x % N, y / 2) : x * powMod(x, y - 1) % N;
	}

	private long secretKeyGen(long x, long y) {
		long r0 = x, r1 = y, r2 = r0 % r1, k = r0 / r1;
		long a = 0, b = 1, c = 1, d = -k, e, f;

	    while (r2 != 0) {
	        r0 = r1;
	        r1 = r2;
	        r2 = r0 % r1;
	        k = r0 / r1;
	        e = a;
	        f = b;
	        a = c;
	        b = d;
	        c = e - k * c;
	        d = f - k * d;
	    }

	    while (b <= 0) b += x;
	    return b;
	}
}
