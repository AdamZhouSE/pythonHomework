T = int(input())
for ttt in range(T):
    n = int(input())
    heightList = [int(i) for i in input().strip().split()]
    left_ptrList = [-1] * n
    right_ptrList = [-1] * n
    stack = []
    i = 0
    while i < n:
        if not stack or heightList[stack[-1]] <= heightList[i]:
            stack.append(i)
            i += 1
        else:
            current = stack.pop()
            left_ptrList[current] = stack[-1] + 1 if stack else 0
            right_ptrList[current] = i
    for i in range(len(stack)):
        if i == 0:
            left_ptrList[stack[i]] = 0
        else:
            left_ptrList[stack[i]] = stack[i - 1]
        right_ptrList[stack[i]] = n
    print(max([heightList[i] * (right_ptrList[i] - left_ptrList[i]) for i in range(n)]))