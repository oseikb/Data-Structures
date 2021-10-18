# Data-Structures
 Python Practice for DS
LinkedLists:

The initial construction of the singly linkedlist was done to illustrate the unidirectional nature in which they operate. 
The only methods included were to insert_node(at the end), add_first, return_last_node, find_node and delete_node.

Doubly linkedlist was built upon the framework of the singly linkedlist by including previous in the node class and also a reference to the last node in the list (the tail)
The methods included in this class were insert_node, add_first, traverse_right, traverse_left, find_node and delete_node

Circular linkedlist was also built using the framework of the singly linkedlist. The major difference is the reference to the first node at the end of the list.
The methods included in this were insert_node, add_first, return_last_node and delete_node.
Traversing the linkedlist in this instance needed to be amended because there will never be a None value in the last node to indicate the end of a list.
Deleting a node needed to be adjusted and edge cases considered for each type of linkedlist with doubly_linkedlist being the simplest implementation and Circular_LinkedList being the most difficult
