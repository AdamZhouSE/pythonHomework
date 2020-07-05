class Node:
    def __init__(self,no,orz):
        self.no = no
        self.orz = orz
        self.next = next
        self.tag = 0
    def setNext(self,next):
        self.next = next
    def printOrz(self):
        stack = []
        node = self
        count = 0
        while node.tag != 1:
            node.tag = 1
            count += node.orz
            stack.append(node)
            node = node.next
        while len(stack) > 0:
            node = stack.pop()
            node.tag = 0
        print(count)

def solve(n,orzF,arr):
    for x in range(n):
        orzF[x].setNext(orzF[arr[x]])
    for x in range(n):
        orzF[x].printOrz()

n = int(input())
temp = input().split(" ")
orzF = []
for x in range(len(temp)):
    orzF.append(Node(x,int(temp[x])))
arr = [int(x)-1 for x in input().split(" ")]
solve(n,orzF,arr)




















