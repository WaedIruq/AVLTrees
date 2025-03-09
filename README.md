AVLTrees Implementation

This repository contains an implementation of an AVL Tree-based list data structure, called AVLTreeList. The AVLTreeList extends the functionality of a basic list by organizing the elements in an AVL tree, providing efficient operations like insertion, deletion, searching, sorting, and more.

Features

The AVLTreeList class provides the following methods:

1. length()

Description: Returns the size of the list (i.e., the number of elements).
Complexity: O(1)
2. sort()

Description: Sorts the elements of the list using QuickSort and returns a new sorted AVL tree.
Complexity: O(n log n)
Returns: An AVLTreeList where the values are sorted.
3. permutation()

Description: Randomly permutes the elements of the list and returns a new AVL tree with the permuted values.
Complexity: O(n log n)
Returns: An AVLTreeList where the values are permuted randomly.
4. concat(lst)

Description: Concatenates another AVLTreeList (lst) to the current list, combining them into one AVL tree.
Complexity: O(log n)
Returns: The absolute value of the height difference between the two trees after concatenation.
5. search(val)

Description: Searches for a given value (val) in the list.
Complexity: O(n)
Returns: The index of the first occurrence of the value, or -1 if not found.
6. getRoot()

Description: Returns the root node of the tree.
Complexity: O(1)
Returns: The root node, or None if the tree is empty.
Helper Methods

1. select(node, i)

Description: Finds the node with the i-th rank (i.e., the node at the i-th position in the in-order traversal).
Complexity: O(log n)
2. successor(node)

Description: Finds the in-order successor of the given node.
Complexity: O(log n)
3. predecessor(node)

Description: Finds the in-order predecessor of the given node.
Complexity: O(log n)
4. BF_q(node)

Description: Computes the balance factor of a node.
Complexity: O(1)
5. func(q, BF)

Description: Determines the number of rotations needed based on the balance factor to maintain AVL tree properties.
Complexity: O(1)
6. rotate(B, D)

Description: Performs a single rotation (either left or right) to maintain balance.
Complexity: O(1)
7. create_node(val)

Description: Creates a new node with the specified value.
Complexity: O(1)
8. join(lst, node)

Description: Merges two AVL trees (self and lst) into one, maintaining the AVL tree properties.
Complexity: O(log n)
How to Use

Example:

# Create an instance of AVLTreeList
tree_list = AVLTreeList()

# Insert elements into the tree
tree_list.insert(0, "apple")
tree_list.insert(1, "banana")
tree_list.insert(2, "cherry")

# Get the length of the list
print(tree_list.length())  # Output: 3

# Sort the list
sorted_tree = tree_list.sort()

# Search for an element
index = tree_list.search("banana")
print(index)  # Output: Index of "banana" in the list

# Concatenate with another list
another_tree = AVLTreeList()
another_tree.insert(0, "date")
tree_list.concat(another_tree)
