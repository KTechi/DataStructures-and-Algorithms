import numpy as np
import random as rd

# http://www.secg.org/sec2-v2.pdf
# Elliptic Curve Cryptography
class ECC:
    def __init__(self, a, b, p, g, n):
        # y^2 = x^3 + A*x + B (modulo P)
        assert 4*a**3 + 27*b**2 != 0
        self.A = a
        self.B = b
        self.P = p # Prime
        self.G = g
        self.N = n

    def print(self):
        print(f'a = {self.A}')
        print(f'b = {self.B}')
        print(f'P = {self.P}')
        print(f'G = {self.G}')
        print(f'N = {self.N}')

    def add(self, p, q):
        if p == (0, 0):
            return q
        if q == (0, 0):
            return p
        if p[0] == q[0] and (p[1], q[1]) == (0, 0) or\
           p[0] == q[0] and p[1] == (self.P - q[1]):
            return 0, 0

        if p == q:
            div = self.__powMod(2*p[1], self.P - 2)
            phi = div * (3*p[0]**2 + self.A) % self.P
            psi = div * (-3*p[0]**3 - self.A*p[0] + 2*p[1]**2) % self.P
        else:
            div = self.__powMod(q[0] - p[0], self.P - 2)
            phi = div * (q[1] - p[1]) % self.P
            psi = div * (q[0]*p[1] - p[0]*q[1]) % self.P

        ret_x = (phi**2 - p[0] - q[0]) % self.P
        ret_y = (-phi*ret_x - psi) % self.P
        return ret_x, ret_y

    def scale(self, s, g = None):
        if g == None:
            g = self.G
            s %= self.N
        if s == 0:
            return 0, 0

        ret = g
        exp = 1
        while exp != s:
            assert exp < s
            tmp = g
            tmp_exp = 1
            while exp + 2*tmp_exp <= s:
                tmp = self.add(tmp, tmp)
                tmp_exp *= 2
            ret = self.add(ret, tmp)
            exp += tmp_exp
        return ret

    def __powMod(self, x, y):
        if y == 0:
            return 1
        return self.__powMod(x * x % self.P, y // 2) if y % 2 == 0 else x * self.__powMod(x, y - 1) % self.P

def Euclide(a, b):
    # ax + by = GCD(a, b)
    # x, y
    u = np.array([1, 0, a])
    v = np.array([0, 1, b])
    while v[2] != 0:
        q = u[2] // v[2]
        u, v = v, u - q * v
    return u[0], u[1]

def moduloInverse(a, mod):
    return Euclide(a, mod)[0] % mod

a, b = 0, 3
p = (1<<192) - (1<<32) - (1<<12) - (1<<8) - (1<<7) - (1<<6) - (1<<3) - (1<<0)
g = (0xDB4FF10EC057E9AE26B07D0280B7F4341DA5D1B1EAE06C7D,\
     0x9B2F2F6D9C5628A7844163D015BE86344082AA88D95E2F9D)
n = 0xFFFFFFFFFFFFFFFFFFFFFFFE26F2FC170F69466A74DEFD8D
ecc = ECC(a, b, p, g, n)
assert g[1]**2 % p == (g[0]**3 + a*g[0] + b) % p
assert ecc.scale(n, g=ecc.G) == (0, 0)

while True:
    d = rd.randint(1, n-1) # Secret Key: Random(1, n-1)
    k = rd.randint(1, n-1) # Secret Key: Random(1, n-1)
    h = rd.randint(1, n-1) # hash(message)
    Q = ecc.scale(d)       # Q = dG
    R = ecc.scale(k)       # R = kG
    r = R[0]
    k_inv = moduloInverse(k, n)
    if k * k_inv % n != 1:
        continue
    s = (h + r*d) * k_inv % n
    s_inv = moduloInverse(s, n)
    if s * s_inv % n != 1:
        continue
    break

def printResult():
    print('======== Parameter ========')
    print('a, b =', a, b)
    print('p =', p) # Prime
    print('n =', n) # nG = \infty
    print('d =', d) # Secret Key: Random(1, n-1)
    print('k =', k) # Secret Key: Random(1, n-1)
    print('h =', h) # hash(message)
    print('======== Signature ========')
    print('r =', r) # R = kG
    print('s =', s) # s = (h + rd)/k modulo n
    print('======== Public Key ========')
    print('G =', g[0])
    print('   ', g[1])
    print('Q =', Q[0]) # Q = dG
    print('   ', Q[1])
    print('======== Verification ========')
    tmp1 = ecc.scale(h*s_inv)      # tmp1 = (h/s)G
    tmp2 = ecc.scale(r*s_inv, g=Q) # tmp2 = (r/s)Q
    tmp3 = ecc.add(tmp1, tmp2)     # tmp3 = tmp1 + tmp2 = (h + rd)/s G = kG
    print('1 =', tmp1[0])
    print('   ', tmp1[1])
    print('2 =', tmp2[0])
    print('   ', tmp2[1])
    print('3 =', tmp3[0])
    print('   ', tmp3[1])
    print('R =', R[0])
    print('   ', R[1])
    if tmp3[0] == r:
        print('\033[32m' + 'Authentication succeeded' + '\033[0m')
    else:
        print('\033[31m' + 'Authentication denied' + '\033[0m')
    print('======== End ========')
printResult()
