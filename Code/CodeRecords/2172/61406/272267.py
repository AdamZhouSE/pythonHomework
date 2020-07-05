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

def priority(x):
    if x=='+' or x=='-':
        return 1
    elif x=='*' or x=='/':
        return 2
    elif x=='^':
        return 3
    elif x=='(':
        return 4


T = int(input())
for a in range(0,T):
    string = input()
    result = ""
    stack = Stack()
    for x in string:
        if x.isalpha():
            result = result+x
        else:
            if x==')':
                while stack.peek()!='(':
                    result = result+stack.pop()
                stack.pop()
            elif stack.is_empty() or priority(stack.peek())<priority(x) or stack.peek()=='(':
                stack.push(x)
            else:
                while not stack.is_empty() and stack.peek()!='(' and priority(stack.peek())>=priority(x):
                    result = result+stack.pop()
                stack.push(x)
    while not stack.is_empty():
        result = result+stack.pop()
    print(result)