n=int(input())
result=[]
for i in range(n):
    a=int(input())
    s=input().split(" ")
    height=[]
    for j in range(a):
        if s[j]>='0' and s[j]<='9':
            height.append(int(s[j]))
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