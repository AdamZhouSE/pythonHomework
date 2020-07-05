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
    s = input()
    stack = Stack()
    for x in s:
        if x.isdigit():
            stack.push(x)
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.push(str(eval(num1+x+num2)))
    print(stack.pop())