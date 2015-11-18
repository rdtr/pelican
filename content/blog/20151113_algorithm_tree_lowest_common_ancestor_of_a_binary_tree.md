Title: Exploring Alrorithm: Lowest Common Ancestor of a Binary Tree
Date: 2015-11-13 00:00
Modified: 2015-11-13 00:00
Category: Algorithm
Tags: algorithm, tree
Slug: algorithm_tree_lowest_common_ancestor_of_a_binary_tree
Authors: rdtr

#### Problem
This problem is from [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/).

```
Given a binary tree, find the lowest common ancestor (LCA)
of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
"The lowest common ancestor is defined between two nodes
v and w as the lowest node in T that has both v and w as descendants
(where we allow a node to be a descendant of itself)."

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
         
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.  
Another example is LCA of nodes 5 and 4 is 5, since a node can be a
descendant of itself according to the LCA definition.
```

#### Solution
Let's say one node is `P` and another is `Q`. To solve this problem, first we construct a map that has each node in a tree as a key, and its parent as a value. Then you can trace the tree from `P` to root, and `Q` to root. Then what we have to do is find the last common node between these two paths.
If we check each node in paths one by one, it takes `O(MN)`(`M`, `N` are a length of each path). To reduce the complexitiy, we can create a hashmap of one path and iterate another, while checking each node exists on the hashmap.

Python code:

[gist:id=79ededfabce2585720f7,file=algorithm_tree_lowest_common_ancestor_of_a_binary_tree_1.py]

Java code:

[gist:id=a93dacc41db72e192211,file=algorithm_tree_lowest_common_ancestor_of_a_binary_tree_1.java]

Time complexicity: `O(K)` while K is a number of elements in a tree given, because we have to check all nodes while constructing a node->parent hashmap.  
Space complexicity is also `O(K)` because we need as many space as a number of nodes to store node->parent hashmap.

It's also possible that we store all paths from root to `P` and root to `Q` as an array individually. In this case, we can iterate both arrays from the first element (which should be the root of the tree) and if an element becomes different between these 2 arrays, the lowest common ancestor would be exactly the previous element of it.

Python code: 

[gist:id=48066cd1198befd70371,file=algorithm_tree_lowest_common_ancestor_of_a_binary_tree_2.py]

Java code:

[gist:id=96974e8fe4ed587eb7cb,file=algorithm_tree_lowest_common_ancestor_of_a_binary_tree_2.java]

It's important to remove the last element at the last line of the recurrsive `findPath` / `constructPath` method. This restores elements of a path array when getting back from a wrong node.

 