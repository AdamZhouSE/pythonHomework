total = int(input())
nums = list(map(int,input().split(' ')))
res = 0
pos = 0
neg = 0
zero = 0
for i in range(0,total):
    if nums[i]>0:
        res+=abs(1-nums[i])
        pos+=1
    elif nums[i]<0:
        res+=-1-nums[i]
        neg+=1
    else:
        res+=1
        zero+=1
if neg%2!=0:
    if zero!=0:
        print(res)
    else:
        res+=2
        print(res)
else:
    print(res)