# dizzy

## prompt
```md
My HEAD is spinning

flag format : cyberZ{some_text_here}
```

<br>

## hints
```md
read about file head...
```

<br>

## files

- [head.jpg](./assets/head.jpg)

<br>

## solution

The image provided is corrupted. You can realize it by opening the image.

Everything in this chall is pointing towards `file header`.

A file `header` is the starting bytes of a file through which the software or OS understands how to treat the file. It's like an ID to the file to determine it's type.

[Know more](https://en.wikipedia.org/wiki/List_of_file_signatures)

Extension of the given image indicates that the file is a `jpg`

```bash
~$ xxd head.jpg
00000000: bbbb bbbb bbbb bbbb bbbb 0001 0100 0001  ................
00000010: 0001 0000 ffdb 0043 0008 0606 0706 0508  .......C........
```

Checking the hex dump of the image shows that the header has been modified. Here it is `bbbb bbbb bbbb bbbb bbbb`. But for a jpg it should be `ffd8 ffe0 0010 4a46 4946`.

So to change it you can use any hex-editor. I'm using `ghex` here.

Spawn it using the command

```bash
~$ ghex head.jpg
```

Change the header to that of a `jpg` and save the file.

![ghex](./assets/ghex.gif)

Now that the header is corrected, you can try opening the image.

![flag](./assets/modified.jpg)

<br>

## flag
```txt
cyberZ{h34d3rs_c4n_b3_4_h34d4ch3}
```