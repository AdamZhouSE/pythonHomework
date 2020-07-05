from collections import deque
import queue


class Node:
    def __init__(self, value=-1, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def levelPrint(root):
    if root != None:
        q = queue.Queue()
        level = 1
        num = 0
        count = 1
        q.put(root)
        while (q.empty() != True):
            print("Level", end=' ')
            print(level, end=' ')
            print(':', end=' ')
            while (count > 0):
                cur = q.get() 
                count -= 1
                if count!=0:
                    print(cur.value, end=' ')
                else:
                    print(cur.value, end='')
                if (cur.left != None):
                    q.put(cur.left)
                    num += 1
                if (cur.right != None):
                    q.put(cur.right)
                    num += 1
            print()
            count = num
            num = 0
            level += 1


def zigzagPrint(root):
    if root != None:
        q = deque()
        level = 1
        num = 0
        count = 1
        q.append(root)
        while (q):
            if (level % 2 == 1):
                print("Level", end=' ')
                print(level, end=' ')
                print('from left to right:', end=' ')
                while (count > 0):
                    cur = q.popleft() 
                    count -= 1
                    if count!=0:
                        print(cur.value, end=' ')
                    else:
                        print(cur.value, end='')
                    if (cur.left != None):
                        q.append(cur.left)
                        num += 1
                    if (cur.right != None):
                        q.append(cur.right)
                        num += 1                    
                print()
                count = num
                num=0
                level += 1
            else:
                print("Level", end=' ')
                print(level, end=' ')
                print('from right to left:', end=' ')
                while (count > 0):
                    cur = q.pop()
                    count -= 1
                    if count!=0:
                        print(cur.value, end=' ')
                    else:
                        print(cur.value, end='')
                    if (cur.right != None):
                        q.appendleft(cur.right)
                        num += 1
                    if (cur.left != None):
                        q.appendleft(cur.left)
                        num += 1
                print()
                count = num
                num=0
                level += 1


arr = list(map(int, input().strip().split(' ')))
n = arr[0]
rootNo = arr[1]
Nodes = []
for i in range(10000):
    Nodes.append(Node(i))

for i in range(n):
    tempA = list(map(int, input().strip().split(' ')))
    if tempA[1] != 0:
        Nodes[tempA[0]].left = Nodes[tempA[1]]
    if tempA[2] != 0:
        Nodes[tempA[0]].right = Nodes[tempA[2]]

levelPrint(Nodes[rootNo])
zigzagPrint(Nodes[rootNo])

