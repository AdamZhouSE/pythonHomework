li = eval(input())
k = int(input())
left = 0
right = len(li)
mid = int((left+right)/2)
while left +1 < right:
    mid = int((left+right)/2)
    if li[mid]==k:
        print(mid)
        exit()
    elif li[mid]>k:
        right=mid
    else:
        left = mid
print(-1)