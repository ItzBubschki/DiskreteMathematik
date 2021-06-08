# Usages:
please note that i'm extremely lazy and i did not want to refactor my code so it may not be beautiful but it works.
## isbn.py:
```python
"Isbn with one missing value (0) or a regular isbn without the checksum (1)?" 0
"Enter isbn with x:" 3x7314903
"Enter checksum:" 9
"The missing number is: 4"
```

or 

```python
"Enter isbn:" 354025782
"The checksum is: 9"
```

## extended_euklid.py
In order to use this script you have to execute `pip3 install prettytable` first
```python
"Enter base num:" 221
"Enter the mod base:" 39
+-----+----+----+---+----+----+
|  a  | b  | r  | q | x  | y  |
+-----+----+----+---+----+----+
| 221 | 39 | 26 | 5 | -1 | 6  |
|  39 | 26 | 13 | 1 | 1  | -1 |
|  26 | 13 | 0  | 2 | 0  | 1  |
+-----+----+----+---+----+----+
"The final result is 38"
```
As you can see in this example it says that your result is 38 while the table say it is -1. <br>
This is due to the fact that you some times need the negative value and some times the positve. and `-1 mod 39 = 38`.

## power_mod.py

```python
"Enter the base num:" 137
"Enter the exponent:" 58
"enter the modulo:" 47
"Phi is 46 and the gcd is 1."
"Do you want to continue with 43(0) or with the negative -4(1)?" 1
"The current exponent is 12. Please enter the new exponents:" 8 4
-4^0 = 1 = 1.
-4^1 = -4 = 43.
-4^2 = 16 = 16.
-4^3 = -64 = 30.
-4^4 = 256 = 21.
-4^5 = -1024 = 10.
-4^6 = 4096 = 7.
-4^7 = -16384 = 19.
-4^8 * -4^4
18 * 21
Result for 137^58%47 = -4^12%47 = 2
```

This is the result if the euler-algorith is possible (if the gcd is 1). <br>
You can decide which base you want to use (positive or negative) and you have to choose the exponents (mainly because i was to lazy to develop something that does that automatically). <br>__The greater exponent has to come first__.

```python
"Enter the base num:" 2
"Enter the exponent:" 61
"enter the modulo:" 22
"The gcd is greater then 1, so the euler algorithm doesn't work."
2^0 = 1 = 1.
2^1 = 2 = 2.
2^2 = 4 = 4.
2^3 = 8 = 8.
2^4 = 16 = 16.
2^5 = 32 = 10.
2^6 = 64 = 20.
2^7 = 128 = 18.
2^8 = 256 = 14.
2^9 = 512 = 6.
2^10 = 1024 = 12.
2^11 = 2
2^61 mod 10 = 2^1 = 2%22 = 2.
```

If the gcd is > 1 the euler-algorithm doesn't work and the program immediatly starts with the exponents