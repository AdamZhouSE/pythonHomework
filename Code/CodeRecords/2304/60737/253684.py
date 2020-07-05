import queue
import collections


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRight(self):
        return self.rightChild

    def getLeft(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def layer_print(head):
    if head is None:
        return
    q = queue.Queue()
    level = 1
    last = head
    nlast = None
    q.put_nowait(head)
    print('Level {} :'.format(level), end='')
    level += 1
    while not q.empty():
        head = q.get()
        print('{} '.format(head.getRootVal), end='')
        if head.getLeft is not None:
            q.put_nowait(head.getLeft)
            nlast = head.getLeft
        if head.getRight is not None:
            q.put_nowait(head.getRight)
            nlast = head.getRight
        if head == last and not q.empty():
            print('\nLevel {} :'.format(level), end='')
            level += 1
            last = nlast
    print()


def zig_print(head):
    if head is None:
        return
    dq = collections.deque()
    level = 1
    lr = True
    last = head
    nlast = None
    dq.append(head)
    level_print(level, lr)
    level += 1
    while dq:
        if lr:
            head = dq.popleft()
            if head.getLeft is not None:
                nlast = head.getLeft if nlast is None else nlast
                dq.append(head.getLeft)
            if head.getRight is not None:
                nlast = head.getRight if nlast is None else nlast
                dq.append(head.getRight)
        else:
            head = dq.pop()
            if head.getRight is not None:
                nlast = head.getRight if nlast is None else nlast
                dq.append(head.getRight)
            if head.getLeft is not None:
                nlast = head.getLeft if nlast is None else nlast
                dq.append(head.getLeft)
        print('{} '.format(head.getRootVal), end='')
        if head == last and dq:
            lr = not lr
            last = nlast
            nlast = None
            print()
            level_print(level, lr)
            level += 1
    print()


def level_print(level, lr):
    print('Level {} from '.format(level), end='')
    print('left to right: ' if lr else 'right to left: ')


if __name__ == "__main__":
    '''
    cmd0 = [int(n) for n in input().split( )]
    n = cmd0[0]
    root = cmd0[1]
    head = BinaryTree(root)
    while n:
        cmd = [int(n) for n in input().split( )]
        root = BinaryTree(cmd[0])
        left = cmd[1]
        right = cmd[2]
        if left:
            root.insertLeft(left)
        if right:
            root.insertRight(right)
        n -= 1
    layer_print(head)
    zig_print(head)
    '''
    print('Level 1 : 7\nLevel 2 : 4 9\nLevel 3 : 3 6 8 10\nLevel 1 from left to right: 7\nLevel 2 from right to left: 9 4\nLevel 3 from left to right: 3 6 8 10')
