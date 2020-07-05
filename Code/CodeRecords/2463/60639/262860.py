nums=list(map(int,input().split(',')))
target=int(input())
judge=0
for i in range(len(nums)-1):
    if judge==1:
        break
    else:
        pass
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print('['+str(i+1)+', '+str(j+1)+']')
            judge=1
            break
        else:
            continue
if judge==0:
    print('None')
else:
    pass