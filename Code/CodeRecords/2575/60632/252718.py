seq = list(input())
stack = []
result = []
for i in seq:
    if i == '(':
        stack.append(i)
        result.append(len(stack)-1)
    else:
        result.append(len(stack)-1)
        stack.pop()
print(result)
