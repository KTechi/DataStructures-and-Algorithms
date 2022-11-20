import random as rd

class ElGamal:
    def __init__(self, p, m):
        self.P = p                             # Public Key: Prime
        self.G = rd.randint(2, p - 2)          # Public Key: Random(2, P - 2)
        self.X = rd.randint(1, p - 2)          # Secret Key: Random(1, P - 2)
        self.Y = self.__powMod(self.G, self.X) # Public Key: G^X (modulo P)
        self.M = m                             # Message: C1^(P-1-X) * C2 (modulo P)
        r = rd.randint(1, p - 2)
        self.C1 = self.__powMod(self.G, r)     # enCode: G^r (modulo P)
        self.C2 = self.__powMod(self.Y, r)*m%p # enCode: M * Y^r (modulo P)

    def print(self):
        print(f'P = {self.P}')
        print(f'G = {self.G}')
        print(f'X = {self.X}')
        print(f'Y = {self.Y}')
        print(f'M = {self.M}')
        print(f'C1 = {self.C1}')
        print(f'C2 = {self.C2}')
        print(f'decode m` = {self.__powMod(self.C1, self.P - 1 - self.X) * self.C2 % self.P}')

    def __powMod(self, x, y):
        if y == 0:
            return 1
        return self.__powMod(x * x % self.P, y // 2) if y % 2 == 0 else x * self.__powMod(x, y - 1) % self.P

elGamal = ElGamal(999999937, 123456789)
elGamal.print()
# print('================')
# elGamal = ElGamal(7572427786695057270624844967644562609112132599800420296747189080920032359205995588384031542287784540006438555802994008688795974493684400576592403320929717,
#                   1111111111222222222233333333334444444444555555555566666666667777777777888888888899999999990000000000)
# elGamal.print()
# 7572427786695057270624844967644562609112132599800420296747189080920032359205995588384031542287784540006438555802994008688795974493684400576592403320929717
# 8609258896430210586523688955272794335561428099377427081622836355194006054569349679983850344916908011330202034512905353365631416251631307084038768336538857
# 9018251874561850467651399512661829039310834429345808807288228370045576292997274498659156953954383290793552486677903139680704353709352146165598701061994853
