"""
题目描述

给定一颗二叉树，分别实现按层和 ZigZag 打印二叉树。 ZigZag遍历: 意思是第一层从左到右遍历，第二层从右到左遍历，依次类推。

输入描述

第一行输入两个整数 n 和 root，n 表示二叉树的总节点个数，root 表示二叉树的根节点。
以下 n 行每行三个整数 fa，lch，rch，表示 fa 的左儿子为 lch，右儿子为 rch。(如果 lch 为 0 则表示 fa 没有左儿子，rch同理)
输出描述

先输出按层打印，再输出按ZigZag打印。
"""


#
#
# # coding:utf-8
# class TreeNode(object):
#     def __init__(self, left=None, right=None, da=0):
#         self.left = left
#         self.right = right
#         self.da = da
#
#
# class BTree(object):
#     def __init__(self, ro=None):
#         self.ro = ro
#
#

def print_by_level1(self):
    if self.root is None:
        return

    q = [(self.root, 1)]
    level = 0
    while q:
        node, lv = q.pop(0)
        if lv != level:
            level = lv
            print()
            print('level', lv, ': ', end='')

        print(node.key, end=', ')
        if node.left:
            q.append((node.left, lv + 1))
        if node.right:
            q.append((node.right, lv + 1))

    print()


def print_zigzag1(self):
    if self.root is None:
        return

    q = [None, self.root]
    level = 0
    print('level', level, ': ', end='')
    while q:
        if level % 2 == 1:
            node = q.pop(0)
        else:
            node = q.pop(-1)

        if node is None:
            print()
            if q:
                level += 1
                if level % 2 == 1:
                    q.append(None)
                else:
                    q.insert(0, None)
                print('level', level, ': ', end='')
        else:
            print(node.key, end=', ')
            if level % 2 == 1:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                if node.right:
                    q.insert(0, node.right)
                if node.left:
                    q.insert(0, node.left)


import random
import operator


class TreeNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None

    def __eq__(self, rhs):
        def recursive(lhs, rhs):
            if lhs is None:
                return rhs is None

            if rhs is None:
                return lhs is None

            if lhs.key != rhs.key or lhs.val != rhs.val:
                return False

            if not recursive(lhs.left, rhs.left):
                return False

            if not recursive(lhs.left, rhs.left):
                return False

            return True

        return recursive(self.root, rhs.root)

    def insert_recursive(self, key, val):
        def recursive(node, key, val):
            if not node:
                return TreeNode(key, val)

            if key < node.key:
                node.left = recursive(node.left, key, val)
            elif key > node.key:
                node.right = recursive(node.right, key, val)

            return node

        self.root = recursive(self.root, key, val)


def test_print():
    # bst = BST()
    line1 = list(map(int, input().split(" ")))
    m = line1[0]
    root = line1[1]
    data = [] * m
    for i in range(m):
        line = list(map(int, input().split(" ")))
        current_data = line
        data.append(current_data)
    nodes = [TreeNode(None, None, 0)] * m
    for i in range(0, nodes.__len__())[::-1]:
        if nodes[i][1] == 0 and nodes[i][2] != 0:
            nodes[i] = TreeNode(None, nodes[i[2]], nodes[i][0])
        elif nodes[i][1] != 0 and nodes[i][2] == 0:
            nodes[i] = TreeNode(nodes[i[1]], None, nodes[i][0])
        elif nodes[i][1] == 0 and nodes[i][2] == 0:
            nodes[i] = TreeNode(None, None, nodes[i][0])
        elif nodes[i][1] != 0 and nodes[i][2] != 0:
            nodes[i] = TreeNode(nodes[i[1]], nodes[i[2]], nodes[i][0])
    bst = BST(nodes[0])
    # keys = []
    # for _ in range(count):
    #     k = random.randint(0, maxkey)
    #     v = k
    #     keys.append(k)
    #     bst.insert_recursive(k, v)
    # 
    # print(keys)
    bst.print_by_level()
    print('---------------------')
    bst.print_zigzag()


if __name__ == '__main__':
    test_print()
