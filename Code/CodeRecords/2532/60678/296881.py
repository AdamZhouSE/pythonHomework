nums = eval(input())
stack = []

for num in nums:
    if stack and num < stack[-1]:
        head = stack.pop()
        while stack and num < stack[-1]:
            stack.pop()
        stack.append(head)
    else:
        stack.append(num)
print(len(stack))