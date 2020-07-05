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


def execute(arr,n):
    # For maintaining distinct elements.
    s = []
    # Initialize ending point and result
    j = 0
    ans = 0
    # Fix starting point
    for i in range(n):
        # Find ending point for current
        # subarray with distinct elements.
        while (j < n and (arr[j] not in s)):
            s.append(arr[j])
            j += 1
        # Calculating and adding all possible
        # length subarrays in arr[i..j]
        ans += ((j - i) * (j - i + 1)) // 2
        # Remove arr[i] as we pick new
        # stating point from next
        s.remove(arr[i])
    return ans


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    info = Input[begin].split()
    N = int(info[0])

    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    begin += 2
    print(execute(arr,N))
