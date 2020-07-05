inp = input()
arr = inp[1:len(inp)-1].split(",")
stack = []
for num in arr:
    if stack and num < stack[-1]:
        head = stack.pop()
        while stack and num < stack[-1]:
            stack.pop()
        stack.append(head)
    else:
        stack.append(num)
res = len(stack)
print(res)