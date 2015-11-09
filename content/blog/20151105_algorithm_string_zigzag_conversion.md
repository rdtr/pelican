Title: Exploring Alrorithm: ZigZag Conversion
Date: 2015-11-07 00:00
Modified: 2015-11-07 00:00
Category: Algorithm
Tags: algorithm, string
Slug: algorithm_string_zigzag_conversion
Authors: rdtr

#### Problem
This problem is from [LeetCode](https://leetcode.com/problems/zigzag-conversion/).

```
The string "PAYPALISHIRING" is written in a zigzag pattern
on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this
conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
```

#### Solution
![example1](http://f.st-hatena.com/images/fotolife/r/rdtr/20151108/20151108232110.png?1447053680)

Let's assign a variable name `t0`, `t1`, `t2` to each string like above, then we immediately see that we need to store each character in a given string in zigzag order (`t0, t1, t2, t1, t0, t1, ...)`.


[gist:id=532ff29a006a086fb1b5,file=algorithm_string_zigzag_conversion.py]

Time complexicity: `O(M)`, space complexicity: `O(M)` while length of the given string = M.

Java code:

[gist:id=bc257df82cb0dd9bb5ae,file=algorithm_string_zigzag_conversion.java]

To make the code efficient, I use StringBuilder on each string concatnation.