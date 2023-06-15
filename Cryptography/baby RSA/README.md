# baby RSA

## prompt

```md
Show your RSA skills!

submit the flag in the following format

**cyberZ{value_of_m}**
```

<br>

## hints

No hints provided

<br>

## files

- [script.py](./assets/script.py)

<br>

## solution

Let's take a look at script

```py
"""

    your task is simple
    1. Learn about RSA
    2. Decrypt the given value of c to get m
    3. Wrap the value of m in cyberZ{}

    example: let's say the value you get is 1500, flag will be
            cyberZ{1500}

"""
```

The script starts with the instructions on how to submit the flag.

```py
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
```

Then it's the RSA implementation in python. The task here is to find the `m` which we don't know. We are given the public key `(N, e)` and the encrypted message `c`.

The thing here is that the `N` is so small that we can factorize it easily. The below script does that for us.

```py
from math import sqrt

N = 5609
p = None
q = None

for i in range(2, round(sqrt(N))):
    if N % i == 0:
        p = N // i
        break

assert p is not None

q = N // p
```

Now that we have `p` and `q` the prime factors of the `N` we can get the private key `d` and thereby decrypt the `c`.

```py
p = 71
q = 79
N = 5609
e = 31
c = 1539

tot = (p - 1) * (q - 1)
d = pow(e, -1, tot)

m = pow(c, d, N)

print(m)
```

Now wrap the obtained value of `m` in flag format `cyberZ{}` to get the flag

<br>

## flag

```txt
cyberZ{4919}
```
