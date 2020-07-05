total = int(input())
nums = list(map(int,input().split(' ')))
i,start,end = 0,-1,-1
while i<total:
    if nums[i] == 0:
        i+=1
        continue
    start = i
    break
if start == -1:
    print(0)
else:
    i = 0
    while i<total:
        if nums[total-1-i] == 0:
            i+=1
            continue
        end = total-1-i
        break
    res = 1
    i = start
    while i < end:
        tem = 1
        if nums[i]==1:
            i+=1
            while i<end and nums[i]==0:
                tem+=1
                i+=1
            res = res*tem
    print(res)