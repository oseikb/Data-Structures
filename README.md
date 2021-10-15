# Data-Structures
 Python Practice for DS
LinkedLists:

The initial construction of the singly linkedlist was done to illustrate the unidirectional nature in which they operate. 
The only methods included were to insert(at the end) and add_first.

Doubly linkedlist was built upon the framework of the singly linkedlist by including previous in the node class and also a reference to the last node in the list (the tail)
The methods included in this class were insert, add_first, traverse_right and traverse_left

Cirular linkedlist was also built using the framework of the singly linkedlist. The major difference is the reference to the first node at the end of the list.
The methods included in this were insert and add_first.
Traversing the linkedlist in this instance needed to be amended because there will never be a None value in the last node to indicate the end of a list.