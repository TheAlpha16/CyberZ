# tiny

## prompt

```md
something seems small here

what do you say ?
```

<br>

## hints
No hints provided

<br>

## files

- [script.py](./assets/script.py)
- [output.txt](./assets/output.txt)

<br>

## solution

Let's analyze the script first.

```py
p = getPrime(1024)
q = getPrime(1024)
```

The above snippet generates two **big** random prime numbers. So there is no chance of prime factorization by sheer brute force.

```py
e = 3
```

Here the value of `e` is chosen to be `3`.

```py
N = p * q
m = bytes_to_long(FLAG)
c = pow(m, e, N)
```

Normal implementation of `RSA` in python 

```py
output = f"N = {N} \ne = {e} \nc = {c}"
open('output.txt', 'w').write(output)
```

Writing output to a file.

Now the prompt suggests that something in this script is small. As you might have already guessed, it's `e`. This doesn't affect the security if the flag is big enough and the `N` is **slightly** larger than `flag`.

But here in this case, it is not effective. Because `p` and `q` are of 1024 bit which is not small.

Let's understand the underlying math.

Consider two numbers `a` and `b`

$ a, b \in \mathbb{Z} $

let $ a < b $

if `a` and `b` are such that $ a < b $, then 

```math
a mod b = a
```

In RSA we encrypt the message by computing ciphertext `c` as

```tex
c = m^e mod N
```

If `e` is small there is a chance that

```tex
m^e < N
```

by the property of modulus this means

```tex
m^e mod N = m^e
```

which means

```tex
c = m^e
```

This means taking `e`th root on `c` produces the original message `m`.

$ c ^ \frac{1}{e} = m $

Since e is 3 here $ \sqrt[3]{c} $ should give the flag!!

This is called [Small e attack](q)

Let's script it.

```py
from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot

e = 3
c = 1275046806497322012213...
```

Importing the required functions and declaring values.

```py
m, is_perfect_root = iroot(c, e)
```

`iroot` is a function in `gmpy2` module which returns two values - integer `i`th root of a number and if the root is exact or perfect.

```py
assert is_perfect_root
```

The `assert` statement makes sure that the root is perfect.

```py
flag = long_to_bytes(m).decode()
print(flag)
```

Conversion of message into it's `byte` representation.

[solve script](./assets/sol.py)

<br>

## flag
```txt
cyberZ{ch00s1ng_sm4ll_e_?_m4th_w1ll_n0t_4llow}
```