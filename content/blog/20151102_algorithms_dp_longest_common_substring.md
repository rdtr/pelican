Title: Exploring Alrorithm: Longest common substrings
Date: 2015-11-02 00:00
Modified: 2015-11-02 00:00
Category: Algorithm
Tags: algorithm, dynamic programming 
Slug: algorithms_dp_longest_common_substring
Authors: rdtr

#### Problem
```
Given two strings, return a length of the longest substring.  
e.g) If "abcdefg" and "cdeg" are given, the longest substring is "cde", therefore return 3.   

```

#### Solution
This is a popular DP algorithm problem.

Let's say strings are S1 and S2, a length of each string is M and N.
We can just check all substrings of S1 and check if each substring exist in S2, and return the longest existing substring, but this takes O(M^2*N) time complexitiry.

To reduce the complexity, we store some information in m[M][N] while m[i][j] stores which index of a common substring S1[i] and S2[j] are on. If they are not on any common substring, just store 0.

![example](http://f.st-hatena.com/images/fotolife/r/rdtr/20151102/20151102165321.png?1446512129)

On the example above, m[3][1] = 2 because S1[3] = S2[1] = 'd' and m[2][0] = 1, that is to say, S1[3] and S2[1] is the 2nd index of the common substring.  
In the same way, we can see m[i][j] would be m[i-1][j-1]+1 if S1[i] == S2[j], otherwise 0.

This is the botto-up approach of dynamic programming.

[gist:id=27d975d4b5bfb816d9b5,file=algorithms_dp_longest_common_substring.py]

In this case, the time and space complexity are both O(MN)

Jave version is below:

[gist:id=63f7f2eeab427e013792,file=algorithms_dp_longest_common_substring.java]