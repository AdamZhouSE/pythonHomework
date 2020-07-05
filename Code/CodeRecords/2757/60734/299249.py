import re
class Tree:
    def __init__(self, key):
        self.key = key
        self.weight = 1
        self.left = None
        self.right = None
        self.left_num = 0
        self.right_num = 0

    def insertLeft(self, newNode):
        if not self.left:
            self.left = Tree(newNode)
        else:
            t = Tree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if not self.right:
            self.right = Tree(newNode)
        else:
            t = Tree(newNode)
            t.right = self.right
            self.right = t

    def getNode(self, key):
        q = [self]
        while q:
            tmp = q.pop(0)
            if tmp.key == key:
                return tmp
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
        return None

    def __str__(self):
        return 'id=' + str(self.key) + ' weight=' + str(self.weight) + '  ' + str(self.left_num) + ':' + str(
            self.right_num)

    def renew(self):
        if self.left:
            self.left.renew()
            self.left_num = self.left.left_num + self.left.right_num + 1
        if self.right:
            self.right.renew()
            self.right_num = self.right.left_num + self.right.right_num + 1


def dfs(root: Tree):
    # nocut
    nocut = root.left_num + root.right_num + root.weight

    if root.left and root.right:
        # left
        root.right.weight += root.weight
        cutleft = dfs(root.left)*dfs(root.right)
        root.right.weight -= root.weight

        # right
        root.left.weight += root.weight
        cutright = dfs(root.left)*dfs(root.right)
        root.left.weight -= root.weight
    elif root.left:  # right == None
        root.left.weight += root.weight
        cutright = dfs(root.left)
        root.left.weight -= root.weight
        cutleft = dfs(root.left)*root.weight
    elif root.right:  # left == None
        root.right.weight += root.weight
        cutleft = dfs(root.right)
        root.right.weight -= root.weight
        cutright = dfs(root.right)*root.weight
    else:
        return root.weight
    return max(nocut, cutleft, cutright)


if __name__ == '__main__':
    n = int(input())
    t = Tree(1)
    for i in range(n - 1):
        lst = list(map(int, re.findall(r'\d+',input())))
        parent = t.getNode(lst[0])
        if parent.left == None:
            parent.insertLeft(lst[1])
        else:
            parent.insertRight(lst[1])
    t.renew()
    print(dfs(t))