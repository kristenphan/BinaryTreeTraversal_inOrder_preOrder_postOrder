# Binary Tree Traversal: inOrder, preOrder, and postOrder

__Repository Description:__
<br/>
This repository stores the work as part of the Data Structures and Algorithms specialization courses by University California of San Diego. Course URL: https://www.coursera.org/learn/data-structures/. Code in this repository is written by myself, Kristen Phan.
<br/>
<br/>
__Assignment Description:__
<br/>
Task: You are given a rooted binary tree. Build and output its in-order, pre-order and post-order traversals.
<br/>
<br/>
Input Format: The first line contains the number of vertices 𝑛. The vertices of the tree are numbered
from 0 to 𝑛 − 1. Vertex 0 is the root.
<br/>
<br/>
The next 𝑛 lines contain information about vertices 0, 1, ..., 𝑛−1 in order. Each of these lines contains
three integers 𝑘𝑒𝑦𝑖, 𝑙𝑒𝑓𝑡𝑖 and 𝑟𝑖𝑔ℎ𝑡𝑖 — 𝑘𝑒𝑦𝑖 is the key of the 𝑖-th vertex, 𝑙𝑒𝑓𝑡𝑖 is the index of the left
child of the 𝑖-th vertex, and 𝑟𝑖𝑔ℎ𝑡𝑖 is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have
left or right child (or both), the corresponding 𝑙𝑒𝑓𝑡𝑖 or 𝑟𝑖𝑔ℎ𝑡𝑖 (or both) will be equal to −1.
<br/>
<br/>
Constraints: 1 ≤ 𝑛 ≤ 105; 0 ≤ 𝑘𝑒𝑦𝑖 ≤ 109; −1 ≤ 𝑙𝑒𝑓𝑡𝑖, 𝑟𝑖𝑔ℎ𝑡𝑖 ≤ 𝑛 − 1. It is guaranteed that the input
represents a valid binary tree. In particular, if 𝑙𝑒𝑓𝑡𝑖 ̸= −1 and 𝑟𝑖𝑔ℎ𝑡𝑖 ̸= −1, then 𝑙𝑒𝑓𝑡𝑖 ̸= 𝑟𝑖𝑔ℎ𝑡𝑖. Also,
a vertex cannot be a child of two different vertices. Also, each vertex is a descendant of the root vertex.
<br/>
<br/>
Output Format: Print three lines. The first line should contain the keys of the vertices in the in-order
traversal of the tree. The second line should contain the keys of the vertices in the pre-order traversal
of the tree. The third line should contain the keys of the vertices in the post-order traversal of the tree.
<br/>
<br/>
Time Limits:
language   C C++ Java Python   C#   Haskell JavaScript Ruby Scala
time (sec) 1 1    12     6    1.5     2          6      6    12
<br/>
<br/>
Memory Limit: 512MB.
<br/>
<br/>
Sample 1.
Input:
<br/>
5
<br/>
4 1 2
<br/>
2 3 4
<br/>
5 -1 -1
<br/>
1 -1 -1
<br/>
3 -1 -1
<br/>
Output:
<br/>
1 2 3 4 5
<br/>
4 2 1 3 5
<br/>
1 3 2 5 4
<br/>
<br/>
__Disclaimer__: 
<br/>
If you're currently taking the same course, please refrain yourself from checking out this solution as it will be against Coursera's Honor Code and won’t do you any good. Plus, once you're worked your heart out and was able to solve a particularly difficult problem, a sense of confidence you gained from such experience is priceless :)"
