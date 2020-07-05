class Stack:
    stack = []

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
    stackS = Stack()
    stackM = Stack()
    stackL = Stack()
    for i in string:
        if i == '(':
            stackS.push(i)
        elif i == '[':
            stackM.push(i)
        elif i == '{':
            stackL.push(i)
        elif i == ')':
            if stackS.pop() is None:
                print('not balanced')
                over = True
                break
        elif i == ']':
            if stackM.pop() is None:
                print('not balanced')
                over = True
                break
        elif i == '}':
            if stackL.pop() is None:
                print('not balanced')
                over = True
                break
    if len(stackS.stack) > 0 or len(stackM.stack) > 0 or len(stackL.stack) > 0:
        print('not balanced')
        over = True
    if not over:
        print('balanced')