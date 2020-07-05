# coding=utf-8
import queue


class TreeNode(object):
    def __init__(self, data=None, left=0, right=0):
        self.data = data
        if left != 0:
            self.left = left
        else:
            self.left = 0
        if right != 0:
            self.right = right
        else:
            self.right = 0

    # 这一步是在每次调用某个结点时，自动调用.data的方法
    def __str__(self):
        return str(self.data)


class Solution:
    def createTree(self, root):

        if root.left != 0:
            root.left = num[root.left - 1]
            self.createTree(root.left)
        if root.right != 0:
            root.right = num[root.right - 1]
            self.createTree(root.right)

        return root

    def midTraverse(self, root):

        if root == 0:
            return
        self.midTraverse(root.left)
        ans.append(root.data)
        self.midTraverse(root.right)

    def is_cbt(self, root):
        if root is None:
            return True

        q = [root]
        reach_leaf = False
        while q:
            node = q.pop(0)
            l, r = node.left, node.right
            if l == 0 and r != 0:
                return False

            if (l != 0 or r != 0) and reach_leaf:
                return False

            if l != 0:
                q.append(l)
            if r != 0:
                q.append(r)
            else:
                reach_leaf = True

        return True


if __name__ == "__main__":
    n = int(input())
    num = []
    for i in range(n * n):
        num.append(TreeNode(i + 1, 0, 0))
    ans = []
    cnt = []
    for i in range(n):
        try:
            a, b, c = map(int, input().strip().split())
            num[a - 1] = TreeNode(a, b, c)
            if i == 0:
                root = TreeNode(a, b, c)
                n = root
        except:
            break
    solution = Solution()
    solution.createTree(root)
    solution.midTraverse(root)

    print(' '.join(map(str, ans)), end=' ')
