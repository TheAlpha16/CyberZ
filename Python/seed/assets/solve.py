from base64 import b64decode
from random import seed, shuffle

enc = b"X3RnX25fc20xZGJ0dHJaZTF5MG5fdW5udG0wfWcwaDFkM2RwbnUwX3MxbjExXzM0c3JfdF9nZF9ndXJjdjQxMWdfczRuMGNoew=="
enc = b64decode(enc).decode()
length = len(enc)

init = list(x for x in range(length))
print(length)

seed(0x1337)
shuffle(init)

flag = ""

for i in range(length):
    index = init.index(i)
    flag += enc[index]

print(flag)
