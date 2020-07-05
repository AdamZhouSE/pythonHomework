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
source=[]
for a in range(0,T):
    source.append(input())
for a in range(0,T):
    string = source[a]
    count = 0
    stack = Stack()
    for one in string:
        if one=='(':
            stack.push(one)
        elif one==')':
            if stack.peek()=='(':
                stack.pop()
                count = count+2
    print(count)



