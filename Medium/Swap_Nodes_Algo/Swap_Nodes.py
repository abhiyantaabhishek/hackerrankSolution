#!/bin/python3
# https://www.hackerrank.com/challenges/swap-nodes-algo/problem?isFullScreen=true
import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data_array):
        # print("len(data_array)", len(data_array))
        node_q = deque()
        self.root = Node(1)
        # print("self.root.data", self.root.data)
        node_q.append(self.root)
        # print("node_q[0]", node_q[0].data)
        ind = 0
        while len(node_q):
            # print("ind", ind)
            d = data_array[ind]
            # if d != -1:
            curr_node = node_q.popleft()
            # print("curr_node", curr_node)
            # print("d", d)
            # print("curr_node.data", curr_node.data)
            if d[0] != -1:
                curr_node.left = Node(d[0])
                node_q.append(curr_node.left)
            if d[1] != -1:
                curr_node.right = Node(d[1])
                node_q.append(curr_node.right)
            ind += 1

    def inorder(self):
        in_order_res = []
        stack = deque()
        curr_node = self.root
        while True:
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            elif stack:
                curr_node = stack.pop()
                print(curr_node.data, end=" ")
                in_order_res.append(curr_node.data)
                curr_node = curr_node.right
            else:
                break
        return in_order_res

    def levelorder_(self):
        queue = deque()
        curr_node = self.root
        queue.append(self.root)
        while queue:
            curr_node = queue.popleft()
            # print(curr_node.data, end=" ")
            print("curr_node.data", curr_node.data)
            print("len(queue)", len(queue))
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

    def get_height(self):
        queue = deque()
        curr_node = self.root
        level = 1
        queue.append([self.root, level])
        while queue:
            curr_node, curr_level = queue.popleft()
            if curr_node.left:
                queue.append([curr_node.left, curr_level + 1])
            if curr_node.right:
                queue.append([curr_node.right, curr_level + 1])
        return curr_level

    def levelorder(self, change_level):
        queue = deque()
        curr_node = self.root
        level = 1
        queue.append([self.root, level])
        while queue:
            curr_node, curr_level = queue.popleft()
            # print(curr_node.data, end=" ")
            # print("curr_node.data", curr_node.data)
            # print("curr_level", curr_level)
            if curr_level == change_level:
                curr_node.left, curr_node.right = curr_node.right, curr_node.left
            if curr_node.left:
                queue.append([curr_node.left, curr_level + 1])
            if curr_node.right:
                queue.append([curr_node.right, curr_level + 1])


def swapNodes(indexes, queries):
    t = Tree()
    # print(len(indexes), indexes)
    # print(queries)

    # Write your code here
    t.add(indexes)
    # print("height", t.get_height())
    # t.inorder()
    # print("")
    results = []
    for q in queries:
        for sq in range(q, t.get_height() + 1, q):
            t.levelorder(sq)
        results.append(t.inorder())
        print("")
    return results


if __name__ == "__main__":
    OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output.txt")
    os.environ["OUTPUT_PATH"] = OUTPUT_PATH
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write("\n".join([" ".join(map(str, x)) for x in result]))
    fptr.write("\n")

    fptr.close()
