class Node:
    def __init__(self, data = None):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        elif data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        else:
            print("Value already present")
    
    def find(self,data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True

    def pre_order(self):
        cur_node = self.root
        if cur_node:
            self._pre_order(cur_node)
    
    def post_order(self):
        cur_node = self.root
        if cur_node:
            self._post_order(cur_node)

    def in_order(self):
        cur_node = self.root
        if cur_node:
            self._in_order(cur_node)

    def _post_order(self, cur_node):
        if cur_node is not None:
            self._post_order(cur_node.left)
            self._post_order(cur_node.right)
            print(cur_node.data)
    
    def _pre_order(self, cur_node):
        if cur_node is not None:
            print(cur_node.data)
            self._pre_order(cur_node.left)
            self._pre_order(cur_node.right)
    
    def _in_order(self, cur_node):
        if cur_node is not None:
            self._in_order(cur_node.left)
            print(cur_node.data)
            self._in_order(cur_node.right)

bst = BST()
bst.insert(4)
bst.insert(5)
bst.insert(3)
bst.insert(8)
"""
    4
3       5
            8

"""
print(bst.find(8))
print(bst.find(10))
print("Post Order")
bst.post_order()
print("In Order")
bst.in_order()
print("Pre Order")
bst.pre_order()