# https://www.hackerrank.com/challenges/is-binary-search-tree/problem?isFullScreen=true

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def check_bst(root):
    from collections import deque

    stack = []  # deque()
    # stack.append(root)
    is_bst = True
    curr = root
    last_data = None
    while len(stack) != 0 or curr != None:
        while curr:
            stack.append(curr)
            curr = curr.left
        if len(stack) != 0:
            curr = stack.pop()
        # print(curr.data)
        # print((last_data,curr.data))
        if last_data != None and last_data >= curr.data:
            is_bst = False
        last_data = curr.data
        if curr:
            curr = curr.right
    return is_bst


def check_binary_search_tree_(root):
    return check_bst(root)
