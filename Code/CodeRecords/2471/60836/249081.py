"""
给定一个表达式字符串exp
检查exp中“ {”，“}”，“（“”）”，“ [”，”]”的对和顺序是否正确
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
    st=list(string_list[i])
    stack=Stack()
    result=True

    for ch in st:
        if ch=='[' or ch=='{' or ch=='(':
            stack.push(ch)
        else:
            if stack.isEmpty():
                result=False
                break
            else:
                c=stack.pop()
                if ch==']':
                    if c!='[':
                        result=False
                        break
                elif ch=='}':
                    if c!='{':
                        result=False
                        break
                else:
                    if c!='(':
                        result=False
                        break

    if not result or not stack.isEmpty():
        print("not balanced")
    else:
        print("balanced")