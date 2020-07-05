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
    string = input()
    stack = Stack()
    for x in string:
        if x=='{':
            stack.push(x)
        else:
            if stack.peek()=="{":
                stack.pop()
            else:
                stack.push(x)
    simple =""
    while not stack.is_empty():
        simple = stack.pop()+simple
    if len(simple)%2==1:
        print(-1)
    else:
        left = simple.count('{')
        right = simple.count('}')
        if len(simple)==left or len(simple)==right:
            print(len(simple)//2)
        else:
            if left%2==0:
                print(len(simple)//2)
            else:
                print(left//2+right//2+2)