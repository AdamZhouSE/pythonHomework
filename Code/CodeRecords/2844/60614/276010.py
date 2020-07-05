init=[int(x) for x in input().split()]
length=init[0]
time=init[1]
books=[int(x) for x in input().split()]
nums=[0]*length
for i in range(length):
    remaining=time
    count=0
    for j in range(i,length):
        if books[j]<=remaining:
            remaining-=books[j]
            count+=1
        else:
            break
    nums[i]=count
print(max(nums))