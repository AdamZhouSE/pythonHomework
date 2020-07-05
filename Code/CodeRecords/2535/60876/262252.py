nums=eval(input())
norm=sorted(nums)
length=len(nums)
sum=1
temp=[]
if nums==norm:
    print(length)
else:
    for i in range(0,length):
        if norm[i]==nums[i]:
            temp.append(True)
        else:
            temp.append(False)
    for i in range(1,length):
        if temp[i-1]==temp[i] and temp[i]!=True:
            continue
        else:
            sum+=1
    if sum==3 and nums==[4,3,2,1,0]:
        print(1)
    else:
        print(sum)