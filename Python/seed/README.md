# seed


## prompt

```md
Every **seed** has it's own way

Retrieve the flag from the script below

**Note**: flag is a python file, which was imported....it is not a module

read [this](https://csatlas.com/python-import-file-module/) for more info
```
<br>

## hints

No hints provided

<br>

## files

- [source.py](./assets/source.py)

<br>

## solution

The intention of this chall is to introduce `random.seed()`.
Usually when we use random module, the actions are random enough not to be predicted.

But using `seed()` sets the state of random function which ensures no matter how many times the code is executed, it generates the same result everytime.

One more thing here is

```py
from flag import FLAG
```

This line doesn't necessarily mean that `flag` has to be a python module. It can be a `.py` file

```py
FLAG = "cyberZ{n0th1ng_1n_c0mput1ng_1s_tru3_r4nd0m_4dd1ng_th1s_t0_4v01d_gu3ss1ng}"
```

Here the code works like this

```py
seed(0x1337) # set the seed
flag_character_list = list(FLAG) # create a list with the flag characters
shuffle(flag_character_list) # shuffle them
shuffled_flag = ''.join(x for x in flag_character_list) # combine the shuffled characters together
print(b64encode(shuffled_flag.encode())) # base64 encode the shuffled flag 
```

So the solution is simple:
  - take a fake flag shuffle it with setting `0x1337` as seed
  - retrace how the characters are being moved
  - combine in that order

```py
enc = b"X3RnX25fc20xZGJ0dHJaZTF5MG5fdW5udG0wfWcwaDFkM2RwbnUwX3MxbjExXzM0c3JfdF9nZF9ndXJjdjQxMWdfczRuMGNoew=="
enc = b64decode(enc).decode()
```

This gives base64 decoded output

```
_tg_n_sm1dbttrZe1y0n_unntm0}g0h1d3dpnu0_s1n11_34sr_t_gd_gurcv411g_s4n0ch{
```

```py
init = list(x for x in range(length)) 

# list init contains numbers equal to the length of the flag [0, 1, 2, 3, ... 71, 72]

seed(0x1337) # set the same seed
```

```py

shuffle(init)

# init after shuffle becomes [27, 31, 71, 30, 12, ... 7, 8, 18, 10, 6]
```

This means the first character in the shuffled flag `_` is 27th character in the actual flag.

Second character `t` is 31st character in the actual flag.

Now that we know which character is at what index we can basically assemble the flag.

```py
for i in range(length):
    index = init.index(i)
    flag += enc[index]
```

The above snippet is finding where the index is in the shuffled list and add that character to flag.

So here the fisrt number `0` is at `59`th index so the 59th character in the shuffled flag `c` is the zeroth character in the actual flag. flag becomes

```
c
```

`1` is at `17`th index so the 17th character `y` becomes first character. flag becomes

```
cy
```

`2` is at `10`th index so the 10th character `b` becomes second character. flag becomes

```
cyb
```

Like this you can traceback each character and get the flag.

`solve.py` and `flag.py` are added in `./assets` for reference.


## flag

```txt
cyberZ{n0th1ng_1n_c0mput1ng_1s_tru3_r4nd0m_4dd1ng_th1s_t0_4v01d_gu3ss1ng}
```
