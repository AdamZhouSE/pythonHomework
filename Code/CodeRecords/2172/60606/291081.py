class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, data):
        """
        进栈函数
        """
        self.stack.append(data)

    def pop(self):
        """
        出栈函数，
        """
        return self.stack.pop()

    def gettop(self):
        """
        取栈顶
        """
        return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
def value(c):
    if c=="+" or c=="-":
        return 1
    elif c=="*" or c=="/":
        return 2
    elif c=="^":
        return 3
    elif c=="(":
        return -1
    else:
        return 0

test_num = int(input())
for i in range(test_num):
    result = ""
    symbol = Stack()
    symbol.push("#")
    target = input()
    target+="#"
    j = 0
    c = target[j]
    while c!="#":
        if "a"<=c<="z" or "A"<=c<="Z":
            result+=c
        elif c=="(":
            symbol.push(c)
        elif c==")":
             temp = symbol.pop()
             while temp!="(":
                 result+=temp
                 temp = symbol.pop()
        else:
            while value(c) <= value(symbol.gettop()):
                temp = symbol.pop()
                result+=temp
            symbol.push(c)
        j+=1
        c = target[j]
    while symbol.isEmpty() is not True:
        temp = symbol.pop()
        if temp !="#":
            result+=temp
    print(result)



