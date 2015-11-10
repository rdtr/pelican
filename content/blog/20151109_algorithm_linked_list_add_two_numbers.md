Title: Exploring Alrorithm: Add 2 numbers
Date: 2015-11-09 00:00
Modified: 2015-11-09 00:00
Category: Algorithm
Tags: algorithm, linked list
Slug: algorithm_linked_list_add_two_numbers
Authors: rdtr

#### Problem
This problem is from [LeetCode](https://leetcode.com/problems/add-two-numbers/).

```
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
```

#### Solution
Just begin from a head of each linked list and sum up each element, then carry over `1` if the sum is greater than 9. When one of the lists reaches its tail, we can stop adding a value from the list. Then when both lists reach their end, we stop the process.

Note that when the last sum amount is greater than 9, we have to perform one more carry-over `1` to the tail of the result list.

<code data-gist-id="071f98653affe6a5196c"></code>

Java code:
<code data-gist-id="de121960e6c181dc3337"></code>

Time complexicity: `O(N)`, space complexicity: `O(N)` while N is a length of the longer list between two given.  
To understand easily I store the result in a new linked-list, but actaully we don't need to use a new one, instead just store the result to `l1` or `l2` (That won't affect the result). Then, there is no extra space needed. 