'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:
  0
 / \
1   0
   / \
  1   0
 / \
1   1
credit: https://www.youtube.com/watch?v=7HgsS8bRvjo
'''

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_unival(root):
    if root is None:
        return True
    if root.left and root.left.val != root.val:
        return False
    # Check the parent node's value with the right node
    if root.right and root.right.val != root.val:
        return False
    return is_unival(root.left) and is_unival(root.right)
  
  
def count_univals(root):
    if root is None:
        return 0

    # Get unival trees from left and right
    total_count = count_univals(root.left) + count_univals(root.right)
    # If root node is unival tree add it to the count
    if is_unival(root):
        total_count+=1
    return total_count  

