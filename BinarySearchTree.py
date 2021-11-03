class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, id):
        n = Node(id)
        curr = self.root
        while curr is not None:
            if curr.data > id:
                if curr.left is None:
                    curr.left = n
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = n
                    break
                curr = curr.right
        else:
            self.root = n

    def find(self, key):
        curr = self.root
        while curr is not None:
            if curr.data == key:
                return curr
            elif curr.data > key:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def find_parent(self, key):
        curr = self.root
        parent = None
        while curr is not None:
            if curr.data == key:
                return parent
            elif curr.data > key:
                parent = curr
                curr = curr.left
            elif curr.data < key:
                parent = curr
                curr = curr.right
        return parent

    def get_successor(self, node):
        del_node = self.find(node.data)
        successor = del_node.right
        if successor.left is None:
            return successor
        while successor.left is not None:
            successor = successor.left
        return successor

    def delete(self, key):
        parent = self.find_parent(key)
        node_del = self.find(key)
        if node_del is None:  # node not found
            return None
        elif self.root == node_del:  # node to be deleted is root
            successor = self.get_successor(node_del)
            self.root = successor
            successor.left = node_del.left
            successor.right = node_del.right
        elif node_del.left is None and node_del.right is None:  # has 0 child element
            if parent.data > key:
                parent.left = None
            else:
                parent.right = None
        elif node_del.left is None or node_del.right is None:  # has 1 child element
            if parent.data > key and node_del.left is None:
                parent.left = node_del.right
            elif parent.data > key and node_del.right is None:
                parent.left = node_del.left
            elif parent.data < key and node_del.right is None:
                parent.right = node_del.left
            else:
                parent.right = node_del.right
        else:  # has 2 child elements
            successor = self.get_successor(node_del)
            if successor.right is None:  # successor is a leaf node
                successor.right = node_del.right
            successor.left = node_del.left
            if parent.data > key:
                parent.left = successor
            else:
                parent.right = successor

    def preorder(self, node):
        curr = node
        if curr is not None:
            print(curr.data)
            self.preorder(curr.left)
            self.preorder(curr.right)

    def postorder(self, node):
        curr = node
        if curr is not None:
            self.preorder(curr.left)
            self.preorder(curr.right)
            print(curr.data)

    def inorder(self, node):
        curr = node
        if curr is not None:
            self.preorder(curr.left)
            print(curr.data)
            self.preorder(curr.right)


if __name__ == "__main__":
    my_bst = Tree()
    my_bst.insert(5)
    my_bst.insert(3)
    my_bst.insert(8)
    my_bst.insert(9)
    my_bst.insert(10)
    my_bst.insert(7)
    my_bst.insert(6)
    my_bst.insert(4)
    my_bst.insert(2)
    my_bst.insert(1)
    my_bst.preorder(my_bst.root)
    print("\n")
    my_bst.postorder(my_bst.root)
    print("\n")
    my_bst.inorder(my_bst.root)
    # print(my_bst.find(190))
    # print(my_bst.find(5))
    # print(my_bst.find(2))
    # print(my_bst.find_parent(1))
    # print(my_bst.find(2).data)
    # my_bst.delete(10)
    # print(my_bst.find(6).right)
    # print(my_bst.find(10))
    # print(my_bst.find(3), my_bst.find(5), my_bst.find(8))
    # print(my_bst.find(2), my_bst.find(3), my_bst.find(4))
    # print(my_bst.find(1), my_bst.find(2))


