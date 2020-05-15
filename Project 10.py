# binary BST in python
from collections import deque

class Node: # simple Node class
    def __init__(self, value):
        self.value = value 
        self.right = None
        self.left = None
        

class BinaryTree:
    pre_order_list = [] # appends nodes for pre_order traversal
    in_order_list = [] # appends nodes for in_order traversal
    post_order_list = [] # appends nodes for post_order traversal

    def __init__(self, root):
        self.root = Node(root)

    def size(self):
        check = deque([])
        size = 0

        if (self.root == None):
            return 0
        else:
            check.append(self.root)
            size += 1
            while len(check) > 0:
                node = check.popleft()
                
                if node.left:
                    size += 1
                    check.append(node.left)
                if node.right:
                    size += 1
                    check.append(node.right)
        return size
    
    def height(self, node):
        
        if(node != None):

            height_left = self.height(node.left)
            hieght_right = self.height(node.right)

            return 1 + max(height_left, hieght_right)
        else:
            return -1

    def pre_order(self, node):
        if node != None:
            self.pre_order_list.append(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)
        return self.pre_order_list
    
    def in_order(self, node):
        if node != None:
            self.in_order(node.left)
            self.in_order_list.append(node.value)
            self.in_order(node.right)
        return self.in_order_list
    
    def post_order(self, node):
        if node != None:
            self.post_order(node.left)
            self.post_order(node.right)
            self.post_order_list.append(node.value)
        return self.post_order_list
    
    def level_order(self, node):
        if node != None:
            Queue = deque([])
            level_order_list = []
            Queue.append(node)

            while len(Queue) > 0:
                level_order_list.append(Queue[0].value)
                node = Queue.popleft()

                if node.left != None:
                    Queue.append(node.left)
                if node.right != None:
                    Queue.append(node.right)

        return level_order_list
    
    def reverse_level_order(self, node): # reverse a binary tree. Very similar to level_order
        x = 1
        if node != None:
            Queue = deque([])
            reverse_level_order_list = []
            Queue.append(node)

            while len(Queue) > 0:
                reverse_level_order_list.append(Queue[0].value)
                node = Queue.popleft()

                if node.right != None:
                    Queue.append(node.right)
                if node.left != None:
                    Queue.append(node.left)

        return reverse_level_order_list[::-1]
   
   ############################################################# Unit test #######################################################
   
import unittest
from binary_tree import BinaryTree, Node

class TestBST(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tree = BinaryTree(1)
        cls.tree.root.left = Node(2)
        cls.tree.root.left.left = Node(4)
        cls.tree.root.left.right = Node(5)

    def test_pre_order(self):
        self.assertEqual(self.tree.pre_order(self.tree.root), [1,2, 4, 5])
    def test_in_order(self):
        self.assertEqual(self.tree.in_order(self.tree.root), [4, 2, 5, 1])
    def test_post_order(self):
        self.assertEqual(self.tree.post_order(self.tree.root), [4, 5, 2, 1])
    def test_level_order(self):
        self.assertEqual(self.tree.level_order(self.tree.root), [1,2, 4, 5])
    def test_reverse_level_order(self):
        self.assertEqual(self.tree.reverse_level_order(self.tree.root), [4 , 5, 2, 1])
    def test_size(self):
        self.assertEqual(self.tree.size(), 4)
    def test_height(self):
        self.assertEqual(self.tree.height(self.tree.root), 2)

if __name__ == "__main__":
    unittest.main()

