nums = eval(input())
stack = []
for num in nums:
    if not stack:
        stack.append(num)
    elif stack and (num < stack[-1]):
        head = stack.pop()
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(head)
print(len(stack))