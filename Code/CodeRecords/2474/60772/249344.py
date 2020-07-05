import sys

class StackUnderflow(ValueError): # 栈下溢（空栈访问）
    pass

class Stack:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderflow("空栈异常：in Stack.top()")
        return self._elems[-1]

    def push(self,elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow("空栈异常：in Stack.pop()")
        return self._elems.pop()


def execute(N):
    li = list(N)
    li = li[:len(li)-1]
    stack = Stack()
    count = 0
    for item in li:
        if item == '(':
            stack.push(item)

        if item == ')':
            if not stack.is_empty():
                stack.pop()
                count += 1

    return 2*count



Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    N = Input[begin]
    begin += 1
    print(execute(N))
