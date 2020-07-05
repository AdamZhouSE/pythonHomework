n = eval(input())
res = []
dic = {}
top = ''

for i in range(n):
    s = input()
    if i == 0:
        top = s[0]
    dic.update({s[0]: s[1:]})
stack = []
stack.append(top)
while len(stack) != 0:
    curTop = stack.pop()
    if curTop != '*':
        res.append(curTop)
        tempNode = dic.get(curTop)
        stack.append(tempNode[1])
        stack.append(tempNode[0])
    else:
        continue
print(''.join(res),end='')