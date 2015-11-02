Title: Exploring Alrorithm: Finding the maximum element in binary tree
Date: 2015-11-01 00:20
Modified: 2015-11-01 00:20
Category: Algorithm
Tags: algorithm, trees 
Slug: algorithms_trees_find_maximum_element_in_binary_tree
Authors: rdtr

#### Problem
```
Find maximum element in binary tree.
```

#### Solution
This is a fairy simple and straigt-forward problem.  
Because we eventually have to check all elements in the binary tree (Note: the tree is not a **binary search** tree)

So we can traverse all elements by BFS, compare value everytime we visit a node while storing the max value at that time, then finally return it.

The code would be like:

[gist:id=5a079f9ffb4163763ca1,file=algorithms_trees_find_maximum_element_in_binary_tree_01.py]
    
The time complexicity is O(N) while N is a number of nodes of the tree, and the space complexicity is also O(N) (Imagine a case that root has all nodes as children). 

Or we can use recurrsive function that searches the biggest number among the node itself, its left child, and right child from a given node.

[gist:id=4460ee20c03761dafd1b,file=algorithms_trees_find_maximum_element_in_binary_tree_02.py]
    
The time complexicity and the space complexicity are both O(N) in this case too.

Java version of the code above is:

[gist:id=cc7affcd8b783e06fe45,file=algorithms_trees_find_maximum_element_in_binary_tree_01.java]

Using recurrsive function:

[gist:id=0d705e57a6a885d1241e,file=algorithms_trees_find_maximum_element_in_binary_tree_02.java]
