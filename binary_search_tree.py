from dataclasses import dataclass
from typing import Union, TypeAlias, Tuple, Any, List
from queue_array import *

BTree: TypeAlias = Union[None, 'Node']

MaybeInt: TypeAlias = Union[None, int]
MaybeTuple: TypeAlias = Union[None, Tuple[Any, Any]]

@dataclass
class Node:
    key: Any                # key for Node, unique ID
    data: Any               # payload for Node
    left: BTree = None      # left child (Node or None)
    right: BTree = None     # right child (Node or None)

@dataclass
class BinarySearchTree:
    root: BTree = None      # root of BST

    # returns True if tree is empty, else False
    def is_empty(self) -> bool:
        return self.root is None 

    # returns True if key is in a node of the tree, else False
    def search(self, key: Any) -> bool:
        if self.is_empty():
            return False 
        else:
            if key == self.root.key:
                return True
            if key > self.root.key:
                return self.search_helper(self.root.right, key)
            if key < self.root.key:
                return self.search_helper(self.root.left, key)
    def search_helper(self, node: Node, key: Any) -> bool:
            if node is None:
                return False
            elif key == node.key:
                return True
            elif key > node.key and node.right != None:
                return self.search_helper(node.right, key)
            elif key < node.key and node.left != None:
                return self.search_helper(node.left, key)

    # Inserts new node w/ key and data
    # If an item with the given key is already in the BST,
    # the data in the tree will be replaced with the new data
    # Example creation of node: temp = Node(key, data)
    def insert(self, key: Any, data: Any = None) -> None:
        temp = Node(key, data, None, None) 
        if self.root is None:
            self.root = temp
            return None
        else:
            return self.insert_helper(self.root, temp, key, data)
    
    def insert_helper(self,node:Node, temp:Node, key:Any, data: Any) -> None:
        if node is None:
            node = temp
        elif key == node.key:
            node.data = data 
        elif key > node.key:
            if node.right is None:
                node.right = temp
            else:
                return self.insert_helper(node.right, temp, key, data)
        elif key< node.key:
            if node.left is None:
                node.left = temp
            else:
                return self.insert_helper(node.left, temp, key, data)
    # returns tuple with min key and associated data in the BST
    # returns None if the tree is empty
    def find_min(self) -> MaybeTuple:
        if self.is_empty():
            return None
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        return temp.key, temp.data 

    # returns tuple with max key and associated data in the BST
    # returns None if the tree is empty
    def find_max(self) -> MaybeTuple:
        if self.is_empty():
            return None
        temp = self.root
        while temp.right is not None:
            temp = temp.right
        return temp.key, temp.data 

    # return the height of the tree
    # if tree is empty, return None
    def tree_height(self) -> MaybeInt:
        if self.is_empty():
            return None
        return self.tree_height_helper(self.root)
            
    def tree_height_helper(self, node: Node) -> MaybeInt:
        if node is None:
            return -1
        else:
            l_height = self.tree_height_helper(node.left)
            r_height = self.tree_height_helper(node.right)
            return max(r_height, l_height) + 1 


    # return Python list of BST keys representing inorder traversal of BST
    def inorder_list(self) -> List:
        list = []
        self.inorder_list_helper(self.root, list)
        return list 
    
    def inorder_list_helper(self, node: Node, list: List) -> List:
        if node is None:
            return None
        else:
            self.inorder_list_helper(node.left, list)
            list.append(node.key)
            self.inorder_list_helper(node.right, list)
    
    # return Python list of BST keys representing preorder traversal of BST
    def preorder_list(self) -> List:
        list = []
        self.preorder_list_helper(self.root, list)
        return list
        
    def preorder_list_helper(self, node: Node, list: List) -> List:
        if node is None:
            return None
        else:
            list.append(node.key)
            self.preorder_list_helper(node.left, list)
            self.preorder_list_helper(node.right, list)


    # return Python list of BST keys representing level-order traversal of BST
    # You MUST use your queue_array data structure from lab 3 to implement this method
    def level_order_list(self) -> List:
        q = Queue(25000)  # Don't change this!
        list = []
        if self.is_empty():
            return list
        q.enqueue(self.root)
        while not q.is_empty():
            temp: Node = q.dequeue()
            list.append(temp.key)
            if temp.left is not None:
                q.enqueue(temp.left)
            if temp.right is not None:
                q.enqueue(temp.right)
        return list