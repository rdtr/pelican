Title: Exploring Alrorithm: Find the Nth element from the tail of the linked list
Date: 2015-11-04 00:00
Modified: 2015-11-04 00:00
Category: Algorithm
Tags: algorithm, linked list 
Slug: algorithm_linkedlist_find_nth_from_tail
Authors: rdtr

#### Problem

```
Return N th node from the end of a linked list. 
If not found, return NULL.
```

#### Solution

One easy solution you may first think up is just go throuth the list to the end once, so you can get the length of the list M, so now you see that the element is `(N - M + 1) th` element from the head of the list.

Python code:

[gist:id=cf9352b2de4426123b22,file=algorithm_linkedlist_find_nth_from_tail_1.py]

Time complexicity: `O(M)`, space complexicity: `O(1)`

Java code:

[gist:id=adc8dfd62d804040d9b7,file=algorithm_linkedlist_find_nth_from_tail_1.java]


This is one way to solve the problem, but we have to go through the same list twice.  
To avoid this, we can use two pointers p1 and p2. First we let p1 proceed to Mth point from the head, then set p2 to the head and let p1 and p2 one by one, until p1 reaches to the tail.  
At this time, p2 is on the Nth point from the tail.

Python code:

[gist:id=e2a828391a72d1cffc64,file=algorithm_linkedlist_find_nth_from_tail_2.py]

This code searches through the given list only once.
Time complexicity: `O(M)`, space complexicity: `O(1)`

Java code:

[gist:id=6aefaad40e61a916f667,file=algorithm_linkedlist_find_nth_from_tail_2.java]

Like this problem, using two pointers and let them run through the same list with a different pace or position is sometime useful way to solve the problem.