class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    #返回栈顶元素
    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items)-1]


T = int(input())
for a in range(0,T):
    row1 = input().split(' ')
    n = int(row1[0])
    k = int(row1[1])
    array = input().split(' ')
    stack = Stack()
    result = ""
    index = 0
    ptr = 0
    while index<n:
        while ptr+index<n and ptr<k:
            stack.push(array[ptr+index])
            ptr+=1
        while ptr>0:
            result = result+" "+stack.pop()
            ptr-=1
        index+=k
    result = result+" "
    print(result.lstrip(' '))
