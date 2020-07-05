class Stack:
    def __init__(self):
        self.lst = [None for i in range(1000)]
        self.top = -1

    def push(self, data):
        if not self.top == len(self.lst) - 1:
            self.top += 1
            self.lst[self.top] = data

    def pop(self):
        if self.top == -1:
            return None
        else:
            data = self.lst[self.top]
            self.top -= 1
            return data

def isBalanced(exp):
    s = Stack()
    for c in exp:
        if c == '[' or c == '{' or c == '(':
            s.push(c)
        elif c == ']':
            data = s.pop()
            if data != '[':
                return 'not balanced'
        elif c == '}':
            data = s.pop()
            if data != '{':
                return 'not balanced'
        elif c == ')':
            data = s.pop()
            if data != '(':
                return 'not balanced'
    if s.top != -1:
        return 'not balanced'
    return 'balanced'

t = int(input())
for i in range(0, t):
    exp = input()
    res = isBalanced(exp)
    print(res)
