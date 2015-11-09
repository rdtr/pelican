Title: Exploring Alrorithm: String matching: brute force
Date: 2015-11-04 00:00
Modified: 2015-11-04 00:00
Category: Algorithm
Tags: algorithm, string 
Slug: algorithms_string_matching_brute_force
Authors: rdtr

#### Problem

```
Check whether string T is a substring of another string S.  
If true, return the first index of where it matches, otherwise return -1.
Example: If S = "ABCDE" and T = "CD", a return value is 2.
```

#### Solution
We can solve this more efficient way, but first let me write about the basic way, brute force.

![example1](http://f.st-hatena.com/images/fotolife/r/rdtr/20151106/20151106184126.png?1446864100)

We will just loop through each index in S, and every time we reach one index i,   
we check whether `S[i] == T[0], S[i+1] == T[1], ...` until the end of T.
If we can reach to the end of T, that means we find T in S, so we return i. Otherwise proceed to next index.

[gist:id=3e49c58fe5c99dff6bf3,file=algorithms_string_matching_brute_force.py]

Time complexicity is `O(MN)` while M and N is the length of each string.
Space complexicity is `O(1)`.

Code in Java is below:

[gist:id=839d3aadea449ecb7e01,file=algorithms_string_matching_brute_force.java]