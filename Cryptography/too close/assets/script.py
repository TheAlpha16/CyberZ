from Crypto.Util.number import bytes_to_long,  getPrime
from sympy import nextprime
from flag import FLAG

p = getPrime(1024)
q = p

for i in range(100):
    q = nextprime(q)

N = p * q
m = bytes_to_long(FLAG)
e = 0x10001
c = pow(m, e, N)

to_be_given = f"N = {N} \ne = {e} \nc = {c}"
open("output.txt", "w").write(to_be_given)
