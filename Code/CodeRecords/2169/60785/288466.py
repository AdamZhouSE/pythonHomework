class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
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
if __name__=="__main__":
    t = int(input())
    for test in range(t):
        s=input()
        res = postfix_calculate(s)
        print(res)