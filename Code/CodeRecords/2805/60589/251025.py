n=int(input())
a=input().split(' ')
a=list(map(int,a))
left=0
right=0
maxLen=1
while right<n:
    tempLen=right-left+1
    if right+1<n and a[right+1]>a[right]:
        right+=1
        tempLen+=1
        if tempLen>maxLen:
            maxLen=tempLen
    else:
        right+=1
        left=right
print(maxLen)