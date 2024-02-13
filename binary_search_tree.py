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
        pass

    # returns True if key is in a node of the tree, else False
    def search(self, key: Any) -> bool:
        pass

    # Inserts new node w/ key and data
    # If an item with the given key is already in the BST,
    # the data in the tree will be replaced with the new data
    # Example creation of node: temp = Node(key, data)
    def insert(self, key: Any, data: Any = None) -> None:
        pass

    # returns tuple with min key and associated data in the BST
    # returns None if the tree is empty
    def find_min(self) -> MaybeTuple:
        pass

    # returns tuple with max key and associated data in the BST
    # returns None if the tree is empty
    def find_max(self) -> MaybeTuple:
        pass

    # return the height of the tree
    # if tree is empty, return None
    def tree_height(self) -> MaybeInt:
        pass

    # return Python list of BST keys representing inorder traversal of BST
    def inorder_list(self) -> List:
        pass

    # return Python list of BST keys representing preorder traversal of BST
    def preorder_list(self) -> List:
        pass

    # return Python list of BST keys representing level-order traversal of BST
    # You MUST use your queue_array data structure from lab 3 to implement this method
    def level_order_list(self) -> List:
        q = Queue(25000)  # Don't change this!
        pass
