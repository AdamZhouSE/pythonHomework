import sys

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        # 判断是否为空
        return self.items == []

    def push(self, item):
        # 压入一个元素，无返回值
        self.items.append(item)

    def pop(self):
        # 弹出一个元素
        return self.items.pop()

    def peek(self):
        # 返回top元素，不改变原Stack
        return self.items[len(self.items) - 1]

    def size(self):
        # 返回Stack的大小
        return len(self.items)


def postfix_calculate(s):
    """注意-号和/号的顺序问题"""
    stack = Stack()
    for x in s:
        if x.isdigit():
            stack.push(x)
        elif x == "+":
            a = stack.pop()
            b = stack.pop()
            stack.push(int(a) + int(b))
        elif x == "-":
            a = stack.pop()
            b = stack.pop()
            stack.push(int(b) - int(a))
        elif x == "*":
            a = stack.pop()
            b = stack.pop()
            stack.push(int(a) * int(b))
        elif x == "/":
            a = stack.pop()
            b = stack.pop()
            stack.push(int(b) / int(a))

    return stack.peek()

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    #info = Input[begin].split()
    #N = int(info[0])

    s = Input[begin]

    begin += 1

    '''
    str = ""
    for i in range(0,len(s)-1):
        str += s[i]
    '''

    print(postfix_calculate(s))
    # execute(s,len(s))
