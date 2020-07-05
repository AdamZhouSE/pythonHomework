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

def handle(num, s):
    x = int(num.pop())
    y = int(num.pop())
    if s == "+":
        return x + y
    elif s == "-":
        return y - x
    elif s == "*":
        return x * y
    elif s == "/":
        return y / x


test_num = int(input())
num = Stack()
for i in range(test_num):
    target = input()
    for j in range(len(target)):
        if "0" <= target[j] <= "9":
            num.push(target[j])
        else:
            temp = handle(num, target[j])
            num.push(temp)
    print(num.gettop())
