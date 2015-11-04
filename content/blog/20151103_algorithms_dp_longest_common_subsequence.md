Title: Exploring Alrorithm: Longest common subsequence
Date: 2015-11-03 00:00
Modified: 2015-11-03 00:00
Category: Algorithm
Tags: algorithm, dynamic programming 
Slug: algorithms_dp_longest_common_subsequence
Authors: rdtr

#### Problem

```
The longest common subsequence of string S1 and S2 is the longest group of
character elements from S1 and S2 that are common between the two groups and
in the same order in each group.
For example, the sequences "1224533324" and "69283746" have an LCS of "234".
```

#### Solution
This is also a popular DP algorithm problem.
It is similar as [Longest Common Substring](http://blog.rdtr.net/posts/2015/11/02/algorithms_dp_longest_common_substring.html) problem, but unlike substrings, **subsequences are not required to occupy consecutive positions within the original sequences**.

Let's consider the example cale of the problem. Now we have a table below, `S1` string is on the row and `S2` is on  the column:

![example1](http://f.st-hatena.com/images/fotolife/r/rdtr/20151103/20151103225640.png?1446620237)

For instance, an orange cell `Table[4][2]` represents the length of LCS of `S1.subString(0, 5) = "12245"` and `S2.subString(0, 3) = "692"`. Our task is fill this table with their each own LCS length.

![example2](http://f.st-hatena.com/images/fotolife/r/rdtr/20151103/20151103230039.png?1446620452)

We can start with the 0th row and 0th column. Regarding the 0th row, this is a problem asking `Does "1224533324" include a character "6"? Mark "0" in the cell until "6" is found and mark "1" after found`. Unfortunately we cannot found `"6"` in this case, then all cells filled with `"0"`. It's the same case in the 0 th column.

![example3](http://f.st-hatena.com/images/fotolife/r/rdtr/20151103/20151103233524.png?1446622533)

Now we proceed to `Table[1][1]`. In this case, `S1[1] != S2[1]` so we have to pick the longest LCS amoung the previous ones, that is `Table[0][1]`, `Table[1][0]`, and `Table[0][0]`. But we can say `Table[0][1] >= Table[0][0]` and `Table[1][0] >= Table[0][0]` because when `S1[1] == S2[0]` or `S1[0] == S2[1]`, `Table[0][1]` or `Table[1][0]` is incremented from `Table[0][0]`. So anyway we can ignore `Table[0][0]` and just check the left cell and the upper cell, then pick the larger one.

![example4](http://f.st-hatena.com/images/fotolife/r/rdtr/20151103/20151103235353.png?1446623644)

Next, `Table[1][2]`. Now `S1[1] == S2[2]` so we can increment the length of the LCS, but at the same time we notice that **we can only jump diagonally from Table[0][1]** because as for `Table[0][2]` and `Table[1][1]`, `S1[1]` or `S2[2]` (= `"2"`) is already taken.

We can generalize the rule as follows:

```
Table[i][j] =
	Table[i-1][j-1] + 1 if S1[i] == S2[j]
	else
		Max(Table[i][j-1], Table[i-1][j])
```

By following the rule above, we can fill in the table as below:

![example5](http://f.st-hatena.com/images/fotolife/r/rdtr/20151104/20151104000153.png?1446624166)

Okay we can get the LCS length, but how we can print the LCS itself? Now you know the LCS length is incremented when we jump diagonally. In other words, to collect LCS characters, we have to collect points we have to jump  when creating a table above and reaches to the final LCS.

![example6](http://f.st-hatena.com/images/fotolife/r/rdtr/20151104/20151104013104.png?1446629490)

To check them, we can start with the very bottom right of the table. **At a point which we have to jump to, `S1[i] == S2[j]` should suffice**. Until reach such point, we would just go upper or left cell which have the same LCS value. Then if we find the point, we collect the character on the cell and jump to upper left cell. We continue this procedure until we reach the boundary of the table.

In the example above, `"4"`, `"3"`, `"2"` are collected, this is the LCS in reversed order.


In the code below, I use `m[i][j]` as a memorization of `Table[i][j]`.

[gist:id=49bfe23174988e06b3fb,file=algorithms_dp_longest_common_subsequence.py]

In this case, the time complexity is O(MN) + O(M+N) = O(MN),  
the space complexity is O(MN). (at most the size of m[M][N]).

Jave version is below:

[gist:id=445d25ae1cae3254661c,file=algorithms_dp_longest_common_subsequence.java]