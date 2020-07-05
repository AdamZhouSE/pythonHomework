class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)


myStack = Stack()
s = input().strip()
for i in range(len(s)):
    if s[i] == '(':
        myStack.push(s[i])
    elif s[i] == ')':
        if len(myStack) == 0:
            print('NO',end='')
            exit()
        else:
            myStack.pop()
if len(myStack) == 0:
    print('YES',end='')
else:
    print('NO',end='')
