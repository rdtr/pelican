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
For example, the sequences "1234" and "1224533324" have an LCS of "1234".
```

#### Solution
This is also a popular DP algorithm problem.
It is similar as [Longest Common Substring](http://blog.rdtr.net/posts/2015/11/02/algorithms_dp_longest_common_substring.html) problem, but unlike substrings, **subsequences are not required to occupy consecutive positions within the original sequences**.

First, we can see that this problem can be solved by induction method.
Let's say `LCS(x, y)` is the length of LCS at the time when you read the data through S1[0] to S1[x], and S2[0] to S2[y].  

##### case1. S1[i] == S2[j]
We can increment the length of LCS only when there is a common character both in S1 and S2, thus the following equation suffices.

![example1](http://f.st-hatena.com/images/fotolife/r/rdtr/20151103/20151103115318.png?1446580546)

##### case2. S1[i] != S2[j]
In this case, we cannot increment the LCS length so just pick the longest LCS among previous ones.

![example2](http://f.st-hatena.com/images/fotolife/r/rdtr/20151103/20151103115442.png?1446580631)

The above equation suffices because  
`LCS(i-1, j-1) <= LCS(i-1, j)` and `LCS(i-1, j-1) <= LCS(i, j-1)`.  
(because the LCS length can be incremented if `S1[i-1] == S2[j]` or `S1[i] == S2[j-1]`.)

So we can memorize all LCS(i, j) values in a 2 dimentional matrix like `m[i][j]` and calculate all possible length while incrementing i and j.

[gist:id=49bfe23174988e06b3fb,file=algorithms_dp_longest_common_subsequence.py]

We also revisit m[i][j] to print the LCS. We can start from the end of each string and gradually move to the frond while picking up the greater `m[i][j]`, and collect a character whenever we find the common one from both strings.

In this case, the time complexity is O(MN) + O(M+N) = O(MN),  
the space complexity is O(MN). (at most the size of m[M][N]).

Jave version is below:

[gist:id=445d25ae1cae3254661c,file=algorithms_dp_longest_common_subsequence.java]