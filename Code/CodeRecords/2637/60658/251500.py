li = eval(input())
left = 0
right = len(li)
mid = 0
while(left<right):
    mid = int((left+right)/2)
    if li[mid]>li[mid+1]:
        right-=1
    else:
        left+=1
print(left)