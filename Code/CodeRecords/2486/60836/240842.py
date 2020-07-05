"""
给出了一个已编码的字符串，任务是对其进行解码
字符串编码的模式如下
原始字符串：abbbababbbababbbab
编码字符串：“ 3 [a3 [b] 1 [ab]]”
"""


class Stack(object):
    """模拟栈"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]


n = int(input())
string_list = []

for i in range(n):
    string_list.append(str(input()))

for i in range(n):
    s_list = list(string_list[i])
    stack=Stack()
    result=""

    for ch in s_list:
        if ch!=']':
            stack.push(ch)    #压栈压进去的是char
        else:
            c=str(stack.pop())
            while c!="[":
                if c.isalpha():
                    result=c+result
                if c.isdigit():
                    result=result*int(c)
                c=stack.pop()

    if not stack.isEmpty():
        c=stack.pop()
        if c.isalpha():
            result = c + result
        if c.isdigit():
            result = result * int(c)

    print(str(result))

