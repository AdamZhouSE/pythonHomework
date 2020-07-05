n=int(input())
result=[]
for i in range(n):
    a=int(input())
    heights=input().split(" ")
    for j in range(a):
        heights[j]=int(heights[j])
    stack = list()

    res = 0

    heights.append(-1)

    for i, h in enumerate(heights):

        while stack and heights[stack[-1]] >= h:
            height_idx = stack.pop()

            pre_idx = stack[-1] if stack else -1

            res = max(res, heights[height_idx] * (i - pre_idx - 1))

        stack.append(i)
    result.append(res)
for f in range(n):
    print(result[f])