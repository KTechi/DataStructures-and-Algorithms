# Rivest Shamir Adleman
class RSA:
    def __init__(self, p, q, m):
        self.P = p                    # Secret Key: Prime
        self.Q = q                    # Secret Key: Prime
        self.N = p*q                  # Public Key: P * Q
        self.L = self.__lcm(p-1, q-1) # Secret Key: Least_Common_Multiple(p-1, q-1)
        # e = 2
        # while self.__gcd(self.L, e) != 1:
        #     e += 1
        # self.E = e
        self.E = 65537 # 2**16+1               # Public Key: Greatest_Common_Divisor(L, E) = 1
        self.D = self.__keyGen(self.E, self.L) # Secret Key: E * D = 1 (modulo L)
        self.M = m                             # Message: C^D (modulo N)
        self.C = self.__powMod(self.M, self.E) # enCode : M^E (modulo N)

    def print(self):
        print(f'P = {self.P}')
        print(f'Q = {self.Q}')
        print(f'N = {self.N}')
        print(f'L = {self.L}')
        print(f'E = {self.E}')
        print(f'D = {self.D}')
        print(f'M = {self.M}')
        print(f'C = {self.C}')
        print(f'decode m` = {self.__powMod(self.C, self.D)}')

    def __gcd(self, x, y):
        return x if y == 0 else self.__gcd(y, x % y)

    def __lcm(self, x, y):
        return x * y // self.__gcd(x, y)

    def __powMod(self, x, y):
        if y == 0:
            return 1
        return self.__powMod(x * x % self.N, y // 2) if y % 2 == 0 else x * self.__powMod(x, y - 1) % self.N

    def __keyGen(self, x, y):
        # return inverse(x, y)
        r0, r1 = y, x
        r2 = r0 %  r1
        k  = r0 // r1
        a, b, c, d, e, f = 0, 1, 1, -k, 0, 0

        while r2 != 0:
            r0 = r1
            r1 = r2
            r2 = r0 % r1
            k = r0 // r1
            e = a
            f = b
            a = c
            b = d
            c = e - k * c
            d = f - k * d
        while b <= 0:
            b += y
        return b

rsa = RSA(999999937, 999727999, 123456789012345678)
rsa.print()
# print('================')
# rsa = RSA(7572427786695057270624844967644562609112132599800420296747189080920032359205995588384031542287784540006438555802994008688795974493684400576592403320929717,
#           8609258896430210586523688955272794335561428099377427081622836355194006054569349679983850344916908011330202034512905353365631416251631307084038768336538857,
#           1111111111222222222233333333334444444444555555555566666666667777777777888888888899999999990000000000)
# rsa.print()
# 9018251874561850467651399512661829039310834429345808807288228370045576292997274498659156953954383290793552486677903139680704353709352146165598701061994853
