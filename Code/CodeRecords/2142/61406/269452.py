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
    result = ""
    count1 = 0
    count2 = 0
    stack = Stack()
    for x in string:
        if x=='(':
            count1 = count1 + 1
            result = result+str(count1)+" "
            stack.push(count1)
        elif x==')':
            if before==')':
                result = result + str(stack.peek()) + " "
                count2 = -1
            else:
                result = result+str(count1)+" "
            count2 = count2 + 1
            stack.pop()
        before = x
    print(result)