n=int(input())
result=[]
for i in range(n):
    a=int(input())
    height=input().split(" ")
    for j in range(a):
        height[j]=int(height[j])
    left = 0
    right = len(height) - 1
    maxarea = 0
    while left < right:
        b = right - left
        if height[left] < height[right]:
            h = height[left]
            left += 1
        else:
            h = height[right]
            right -= 1
        area = b * h
        if maxarea < area:
            maxarea = area
    result.append(maxarea)
for f in range(n):
    print(result[f])