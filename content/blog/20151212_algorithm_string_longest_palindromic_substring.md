Title: Exploring Alrorithm: Longest Palindromic Substring
Date: 2015-12-012 00:00
Modified: 2015-12-12 00:00
Category: Algorithm
Tags: algorithm, string
Slug: algorithm_string_longest_palindromic_substring
Authors: rdtr

#### Problem
This problem is from [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/).

```
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.
```

#### Solution
A palindrome is a string that reads the same backward or forward, like
`CABAC` and `CABBAC`. `CABAC` has an odd length and the center is `B` `CABBAC` has an even length and the center is `BB`. One important fact about a palindrom is, that has line symmetry where the line is a center character (or 2 character when it has an even length).

So, we can iterate each element `S[i]` of the given string, and regard `S[i]` as a center of some palindrome, then we can expand the palindrome one by one, as long as **the left side element and the right side one has the same character** as below.

```
  <-------------------> step3. length = 5
      <----------->     step2. length = 3
          <--->         step1. length = 1

+-+---+---+---+---+---+-+
  |   |   |   |   |   |
  | Y | X |   | X | Y |
  |   |   |   |   |   |
+-+---+---+---+---+---+-+

```

We have to consider also the case a palindrome has an even length. So in the same way, we can regard `S[i]` and `S[i+1]` as a center of a palindrome and try expanding it as below. 

```
     <----------------------> step3. length = 6
         <-------------->     step2. length = 4
             <------->        step1. length = 2
-+---+---+---+---+---+---+---+-
 |   |   |   |   |   |   |   |
 |   | Y | X |   |   | X | Y |
 |   |   |   |   |   |   |   |
-+---+---+---+---+---+---+---+-
```
Note: **S[i] should equal to S[i+1] in this case.**

[gist:id=91c8354250e806a5e717,file=algorithm_string_longest_palindromic_substring.py]

To iterate each element, we should take `O(N)` time comlexity. And each expansion trial takes also `O(N)` at most, so as a whole, time complexicy is `O(N^2)`.  
(To make it little more efficient, I set a break condition at the first line in the iteration loop and prevent keep searching a palindrome if the possible longest palindrome with a center S[i] is never longer than the current max palindrome).

The space complexity is `O(1)` since we don't use extra space.

A code in Java is below:

[gist:id=51c2c1e80d53932ee7a0,file=algorithm_string_longest_palindromic_substring.java]

On this java code, the space complexity is `O(N)` because I use String to hold the current maximum palindrome during an iteration.