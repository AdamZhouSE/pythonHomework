class Tree:
    def __init__(self, value, left=None, right=None):
        self.setLeft(left)
        self.setRight(right)
        self.value = value

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def __str__(self):
        l = ''
        r = ''
        s = str(self.value)
        if self.left.value != '#':
            l = self.left.__str__()
        if self.right.value != '#':
            r = self.right.__str__()
        return str(l + s + r)


def dosth(li):
    li = list(li)
    if li[0] == '#':
        return Tree(li.pop(0)), li
    else:
        t = Tree(li.pop(0))
        t1, li = dosth(li)
        t.setLeft(t1)
        t2, li = dosth(li)
        t.setRight(t2)
        return t, li


s = list(input() + '#############')
t = dosth(s)[0]
t = t.__str__()
t = list(t)
[print(i, end=' ') for i in t]
