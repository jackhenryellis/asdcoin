# asdcoin
`asdcoin.py` is a program that decrypts the multiple layers of encryption present on the [Australian Signal Directorate's 75th Anniversary Commemorative Coin](https://www.asd.gov.au/75th-anniversary/events/2022-09-01-75th-anniversary-commemorative-coin).

## Decryption

### Puzzle 1
The braille letters **CBFAED** are inscribed on the [head side of the coin](https://www.asd.gov.au/sites/default/files/2022-09/ASD-50-SIDE-B-Hires.jpg), under the letters **BTHASA**.
```
E L I Z A B E T H  I I  .  A U S T R A L I A  2 0 2 2  .  5 0  C E N T S
------------------------------------------------------------------------
          C   B F          A   E           D
```

When the braille letters are rearranged into alphabetical order, the letters spell **ATBASH**, hinting to the Atbash substitution cipher.
```
before rotation

B T H A S A
-----------
C B F A E D
```

```
after rotation

A T B A S H
-----------
A B C D E F
```


### Puzzle 2
The ciphertext of the outer ring on the [tails side of the coin](https://www.asd.gov.au/sites/default/files/2022-09/ASD-50-SIDE-A-Hires.jpg) reads
```
.DVZIVZFWZXRLFHRMXLMXVKGZMWNVGRXFOLFHRMVCVXFGRLM.URMWXOZIRGBRM7DRWGSC5WVKGS
```

Each character of the ciphertext can be simply decrypted by using a lookup table for the Atbash cipher, which is a simple reverse alphabet substitution cipher.

```python
# python implementation of an atbash lookup table
atbash = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W',
		  'E' : 'V', 'F' : 'U', 'G' : 'T', 'H' : 'S',
		  'I' : 'R', 'J' : 'Q', 'K' : 'P', 'L' : 'O',
		  'M' : 'N', 'N' : 'M', 'O' : 'L', 'P' : 'K',
		  'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
		  'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C',
		  'Y' : 'B', 'Z' : 'A'}
```

```
ciphertext

.DVZIVZFWZXRLFHRMXLMXVKGZMWNVGRXFOLFHRMVCVXFGRLM.URMWXOZIRGBRM7DRWGSC5WVKGS
--------------------------------------------------------------------------
.WEAREAUDACIOUSINCONCEPTANDMETICULOUSINEXECUTION.FINDCLARITYIN7WIDTHX5DEPTH

plaintext
```

The plaintext reveals two [ASD values](https://www.asd.gov.au/about/values), 
- We are audacious in concept
- We are meticulous in execution

The end of the plaintext reads **FIND CLARITY IN 7 WIDTH X 5 DEPTH**, suggesting the next puzzle can be solved with 7x5 matrices


### Puzzle 3
The ciphertext of the inner ring on the [tails side of the coin](https://www.asd.gov.au/sites/default/files/2022-09/ASD-50-SIDE-A-Hires.jpg) reads
```
BGOAMVOEIATSIRLNGTTNEOGRERGXNTEAIFCECAIEOALEKFNR5LWEFCHDEEAEEE7NMDRXX5
```

When inserted horizontally into a 7x5 matrix, plaintext is readable vertically.
```
B G O A M V O
E I A T S I R
L N G T T N E
O G R E R G X
N T E A I F C
```
*Belonging to a great team striving for exc...*

Since the ciphertext is 70 characters long, a second 7x5 matrix is required
```
E C A I E O A
L E K F N R 5
L W E F C H D
E E A E E E 7
N M D R X X 5
```
*...ellence we make a difference XOR hex A5D75*

The complete ciphertext reads
```
BELONGING TO A GREAT TEAM STRIVING FOR EXCELLENCE WE MAKE A DIFFERENCE XOR HEX A5D75
```

The ciphertext reveals the final three [ASD values](https://www.asd.gov.au/about/values), 
- We belong to a great team
- We strive for excellence
- We make a difference
 
The ciphetext ends in **XOR HEX A5D75** - l33tspeak for ASD 75 and a hint pertaining to the encryption method behind the final puzzle.


### Puzzle 4
A series of hexadecimal values can be found in the lower right portion of the [tails side of the coin](https://www.asd.gov.au/sites/default/files/2022-09/ASD-50-SIDE-A-Hires.jpg)
```
E3B
8287D4
290F723381
4D7A47A291DC
0F71B2806D1A53B
311CC4B97A0E1CC2B9
3B31068593332F10C6A335
2F14D1B27A3514D6F7382F1A
D0B0322955D1B83D3801CDB2
287D05C0B82A311085A03329
1D85A3323855D6BC333119D
6FB7A3C11C4A72E3C17CCB
B33290C85B6343955CCBA3
B3A1CCBB62E341ACBF72
E3255CAA73F2F14D1B27A
341B85A3323855D6BB33
3055C4A53F3C55C7B22
E2A10C0B97A291DC0F
73E3413C3BE392819
D1F73B331185A33
23855CCBA2A3
206D6BE383
1108B
```

2 hexadecimal values can be represented as 1 byte, e.g.
```
hex
E 3

decimal representation of each value
14 3

binary representation of the decimal values
1110 0011
```

The same can be done for the XOR key **A5** D75
```
hex
A 5

decimal representation of each value
10 5

binary representation of the decimal values
1010 0101
```

The Exclusive OR (XOR) logic gate is defined as:
| A | B | A XOR B |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Hence, the XOR operation between hex values E3 and A5 is
```
1 1 1 0 0 0 1 1
1 0 1 0 0 1 0 1
---------------
0 1 0 0 0 1 1 0
```

We can then convert `01000110` to its ASCII counterpart, revealing the first character of the plaintext as the letter **F**
```python
>>> int('01000110', base=2)
70
>>> chr(70)
'F'
```

The entire XOR operation can be done iteratively in Python, first by converting both the plaintext and keystream hex bytes to decimal, then using the bitwise XOR operator `^`
```python
>>> int('E3', base=16)
227
>>> int('A5', base=16)
165
>>> 227^165
70
```

The entire XOR operation, using the repeated hexadecimal keystream of A5D75 and converting the resultant bytes to ASCII, reveals the below plaintext
```
For 75 years the Australian Signals Directorate has brought together people with the skills, adaptability and imagination to operate in the slim area between the difficult and the impossible.
```


## Program Usage

**Solve all puzzles**
```
asdcoin.py --solve
```

**Solve individual puzzles**
```
asdcoin.py --puzzle_one
asdcoin.py --puzzle_two
asdcoin.py --puzzle_three
asdcoin.py --puzzle_four
```
