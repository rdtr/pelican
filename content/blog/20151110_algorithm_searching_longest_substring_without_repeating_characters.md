Title: Exploring Alrorithm: Longest Substring Without Repeating Characters
Date: 2015-11-10 00:00
Modified: 2015-11-10 00:00
Category: Algorithm
Tags: algorithm, string
Slug: algorithm_string_longest_substring_without_repeating_characters
Authors: rdtr

#### Problem
This problem is from [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/).

```
Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc",
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
```

#### Solution
We can solve this problem just one iteration through the string given.  
We use HashMap to check if a character repeats in a previous sequence.

![example](http://f.st-hatena.com/images/fotolife/r/rdtr/20151111/20151111133323.png?1447277616)

An example is shown at above. Until we find a character appears twice we can just increment the current length, then if at index `j` we detect the character is already apperaed at index `i`, the longest substring without repeating characters is `S[i+1]` to `S[j]`.

And in an iteration after this point, we can consider only from at index `i+1`. So we have to store this index as `start_index` of the current longest substring, and if the character appeeared at `k` such that `k < start_index`, we can just ignore that.


[gist:id=fe007f309b254f075fe0,file=algorithm_string_longest_substring_without_repeating_characters.py]

Java code:

[gist:id=867ae29963ac1edf4647,file=algorithm_string_longest_substring_without_repeating_characters.java]

Time complexicity: `O(N)`, space complexicity: `O(N)` while N is a length of the string given.