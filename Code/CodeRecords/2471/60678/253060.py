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
stringTest = ''
for loopTimes in range(0, times):

    over = False
    string = input()

    print('string')
    