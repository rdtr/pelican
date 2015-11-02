Title: アルゴリズム探訪: 二分木から要素の持つ最大値を求める
Date: 2015-11-01 00:20
Modified: 2015-11-01 00:20
Category: Algorithm
Tags: algorithm, trees 
Slug: algorithms_trees_find_maximum_element_in_binary_tree
Lang: jp
Authors: rdtr
Summary: Finding the maximum element in binary tree

#### Problem
```
二分木の各要素が持つ値のうち, 最大のものを求めよ.
```

#### Solution
２分探索木ではないので, 全要素をチェックして最大のものを返却する必要があります.１つ目の解法では幅優先探索で全nodeを走査し, その時点での最大値を見つけるたびにそれを変数に格納しておきます.  
そうすると, 走査が終えた時点でその変数には最大値が格納されていることになります.

[gist:id=5a079f9ffb4163763ca1,file=algorithms_trees_find_maximum_element_in_binary_tree_01.py]
    
計算量は要素数をNとしてO(N), 空間量もO(N)となります(N-1個の子がすべてrootにぶら下がっていた場合, queueにはO(N)の要素数の格納が必要となるため).

あるいは, 親要素を与えられた時に左の子要素達, 右の子要素達から最大値を求めるような関数を定義してやるとこの問題は再帰的に解くこともできます.

[gist:id=4460ee20c03761dafd1b,file=algorithms_trees_find_maximum_element_in_binary_tree_02.py]
    
この場合も計算量, 空間量は同じくO(N)となります.