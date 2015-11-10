Title: Exploring Alrorithm: 2 Sum
Date: 2015-11-08 00:00
Modified: 2015-11-08 00:00
Category: Algorithm
Tags: algorithm, searching
Slug: algorithm_searching_two_sum
Authors: rdtr

#### Problem
This problem is from [LeetCode](https://leetcode.com/problems/two-sum/).

```
Given an array of integers, find 2 numbers such that
they add up to a specific target number.
You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: [1, 2]
```

#### Solution
We can solve this problem by using brote-force method, just check all combination of two elements in a given array, then check their sum. But this takes `O(N^2)` in terms of time complexity.

Instead, while iterating through the array `A`, we can store each element in a hash map as a key. Because finally we have to output an index of each integer, it's natural to store an index as value to the map.  
We can also check if a value such that `value = target - A[i]` exists in the precious indexes by using the map. Then we can iterate through the array only once and can stop searching as soon as we find the solution.

[gist:id=1a29a54c52a1c877c9cb,file=algorithm_searching_two_sum.py]

Time complexicity: `O(N)`, space complexicity: `O(N)` while length of the given array = N.

Java code:

[gist:id=2a2c56335cbe24c8b11a,file=algorithm_searching_two_sum.java]
