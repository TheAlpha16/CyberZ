# vision

## prompt

```md
Can you see the flag ?
```

<br>

## hints

```md
Maybe you need **white** filter to see
```

<br>

## files

- [see_me.txt](./assets/see_me.txt)

## solution

At first glance the file looks empty but taking a closer look at it will reveal that there are some bytes.

```bash
~$ xxd see_me.txt | head -n 5
00000000: 2020 2009 0920 2020 0909 0a09 0a20 2020     ..   .....   
00000010: 2020 0909 0909 2020 090a 090a 2020 2020    ....  ....    
00000020: 2009 0920 2020 0920 0a09 0a20 2020 2020   ..   . ...     
00000030: 0909 2020 0920 090a 090a 2020 2020 2009  ..  . ....     .
00000040: 0909 2020 0920 0a09 0a20 2020 2020 0920  ..  . ...     . 
```

Now the hint suggests some `white` filter. There are only `spaces`, `tabs` and `newline characters` in the given file. This hints that the given file is a [whitespace](https://en.wikipedia.org/wiki/Whitespace_(programming_language)) text.

Using this [tool](https://www.dcode.fr/whitespace-language) you can get the flag.

<br>

## flag

```txt
cyberZ{1'm_1nv1s1bl3_unt1l_y0u_s33_m3}
```