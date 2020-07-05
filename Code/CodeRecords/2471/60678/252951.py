class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        elem = self.stack[len(self.stack) - 1]
        del self.stack[len(self.stack) - 1]
        return elem

    def push(self, elem):
            self.stack.append(elem)

    def top(self):
        return self.stack[len(self.stack) - 1]


times = int(input())
for loopTimes in range(0, times):
    over = False
    string = input()
    stack = Stack()
    for i in string:
        if i == '(' or i == '[' or i == '{':
            stack.push(i)
        elif i == ')':
            character  = stack.pop()
            if character == '[' or character == '{':
                print('not balanced')
                over = True
                break
        elif i == ']':
            character = stack.pop()
            if character == '(' or character == '{':
                print('not balanced')
                over = True
                break
        elif i == '}':
            character = stack.pop()
            if character == '(' or character == '[':
                print('not balanced')
                over = True
                break
    if  not over and len(stack.stack) > 0:
        print('not balanced')
        over = True
        break
    if not over:
        print('balanced')