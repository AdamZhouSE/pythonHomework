questNum = int(input())

for quest in range(questNum):
    n = int(input())
    height = input().split(' ')
    for i in range(n):
        height[i] = int(height[i])
    stack = []
    maxArea = 0
    top = 0
    areaWithTop = 0

    i = 0
    while i < n:
        if len(stack) == 0 or height[stack[len(stack) - 1]] <= height[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if len(stack) == 0:
                temp = i
            else:
                temp = i - stack[len(stack) - 1] - 1
            areaWithTop = height[top] * temp
            maxArea = max(maxArea, areaWithTop)

    while len(stack) != 0:
        top = stack.pop()
        if len(stack) == 0:
            temp = i
        else:
            temp = i - stack[len(stack) - 1] - 1
        areaWithTop = height[top] * temp
        maxArea = max(maxArea, areaWithTop)

    print(maxArea)