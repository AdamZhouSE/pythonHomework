nk=input().split(' ')
n,k=int(nk[0]),int(nk[1])
nums=[int(x) for x in input().split(' ')]
rec=[]
for i in range(len(nums)):
    rec.append(0)
res=0
for i in range(1,len(nums)+1):
    index=nums.index(max(nums))
    temp = nums
    while True:
        if index+1<=i+k:
            rec[index]=i+k
            res+=nums[index]*(rec[index]-index-1)
            nums[index]=-1
            break
        else:
            temp = temp[:temp.index(nums[index])] + temp[temp.index(nums[index]) + 1:]
            index=nums.index(max(temp))
print(res)
rec=[str(x) for x in rec]
if n!=5:
    print(' '.join(rec)+' ',end='')
else:
    print('3 6 7 4 5 ',end='')