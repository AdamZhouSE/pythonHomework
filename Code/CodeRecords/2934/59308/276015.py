from collections import deque

s = input()
stack = deque()
for i in range(len(s)):
    if s[i] != ']':
        stack.appendleft(s[i])
    else:
        temp = ''
        while True:
            if stack[0] != '[':
                temp += stack[0]
                stack.popleft()
            else:
                stack.popleft()
                break
        num = ''
        for j in range(len(temp)-1, -1, -1):
            if temp[j].isdigit():
                num += temp[j]
            else:
                break
        num = int(num)
        temp = temp[:j+1]
        for j in range(num):
            for k in range(len(temp)-1, -1, -1):
                stack.appendleft(temp[k])
print(''.join(reversed(stack)),end='')


