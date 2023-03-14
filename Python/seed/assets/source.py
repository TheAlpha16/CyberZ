from base64 import b64encode
from random import shuffle, seed
from flag import FLAG

seed(0x1337)

flag_character_list = list(FLAG)
shuffle(flag_character_list)

shuffled_flag = ''.join(x for x in flag_character_list)
print(b64encode(shuffled_flag.encode()))

# X3RnX25fc20xZGJ0dHJaZTF5MG5fdW5udG0wfWcwaDFkM2RwbnUwX3MxbjExXzM0c3JfdF9nZF9ndXJjdjQxMWdfczRuMGNoew==
