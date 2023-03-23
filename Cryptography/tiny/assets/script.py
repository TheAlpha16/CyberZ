from Crypto.Util.number import bytes_to_long, getPrime

FLAG = REDACTED

p = getPrime(1024)
q = getPrime(1024)
e = 3

N = p * q
m = bytes_to_long(FLAG)
c = pow(m, e, N)

output = f"N = {N} \ne = {e} \nc = {c}"

open('output.txt', 'w').write(output)