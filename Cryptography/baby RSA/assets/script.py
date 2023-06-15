"""

    your task is simple
    1. Learn about RSA
    2. Decrypt the given value of c to get m
    3. Wrap the value of m in cyberZ{}

    example: let's say the value you get is 1500, flag will be
            cyberZ{1500}

"""

m = REDACTED
p = REDACTED
q = REDACTED
e = 31

N = p * q
c = pow(m, e, N)

print("N =", N)
print("e =", e)
print("c =", c)

# N = 5609
# e = 31
# c = 1539
