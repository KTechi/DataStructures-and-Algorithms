# Binary Search Tree
__Code__
```python
bst = BinarySearchTree()
for i in [7, 4, 8, 3, 5, 9, 1, 6, 0, 2]:
    bst.insert(i)
print(bst.list())
bst.print_tree()
bst.delete(7)
print(bst.list())
bst.print_tree()
```
__Output__
```python
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
       7
    4   8
   3 5   9
 1    6
0 2
[0, 1, 2, 3, 4, 5, 6, 8, 9]
      6
    4  8
   3 5  9
 1
0 2
```

# AVL Tree
__Code__
```python
avl = AVLTree()
for i in [5, 4, 3, 2, 1, 0, 6]:
    avl.insert(i)
print(avl.list())
avl.print_tree()
avl.delete(0)
print(avl.list())
avl.print_tree()
```
__Output__
```python
[0, 1, 2, 3, 4, 5, 6]
  2
 1  4
0  3 5
      6
[1, 2, 3, 4, 5, 6]
   4
 2  5
1 3  6
```
