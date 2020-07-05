arr=eval(input())
stack = []
for num in arr:
            # 递增栈
    if not stack or stack[-1] <= num:
        stack.append(num)
    else:
        cur_max = stack.pop()
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(cur_max)
print(len(stack))