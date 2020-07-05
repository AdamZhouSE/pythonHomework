n = int(input())
heights =[]
for i in range(0,n):
    a =int(input())
    height =input().split(' ')
    for i in range(0,a):
        height[i]=int(height[i])
    heights.append(height)
result =[]
for i in range(0,n):
    height = heights[i]
    k = len(height)
    count=0
    left =0
    right =k-1
    leftheight =0
    rightheight =0
    while left<right:
        if height[left]<=height[right]:
            leftheight=max(leftheight,height[left])
            count+=leftheight-height[left]
            left+=1
        else:
            rightheight = max(rightheight,height[right])
            count+=rightheight -height[right]
            right-=1
    result.append(count)

for i in range(0,len(result)):
    print(result[i])