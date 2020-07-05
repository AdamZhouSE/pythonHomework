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

    def midTraverse(self, root, ans):

        if root == 0:
            return ans
        self.midTraverse(root.left,ans)
        ans.append(root.data)
        self.midTraverse(root.right,ans)

    def test(self, root, ans):
        ans = []
        self.midTraverse(root, ans)
        m = ans
        if sorted(m) == ans:
            cnt.append(len(m))
        ans = []
        if root.left != 0:
            self.test(root.left, ans)
        m = ans
        if sorted(m) == ans:
            cnt.append(len(m))
        if root.right != 0:
            self.test(root.right, ans)
        m = ans
        if sorted(m) == ans:
            cnt.append(len(m))
        return


if __name__ == "__main__":
    n, root = map(int, input().strip().split())
    num = []
    length = 1
    max_len = 1
    cnt = []
    for i in range(n * n):
        num.append(TreeNode(i + 1, 0, 0))
    ans = []
    cnt = []
    for i in range(n):
        try:
            a, b, c = map(int, input().strip().split())
            num[a - 1] = TreeNode(a, b, c)
            if root == a:
                root = TreeNode(a, b, c)
        except:
            break
    solution = Solution()
    solution.createTree(root)
    solution.test(root,ans)

    print(max(cnt))
