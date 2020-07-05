num_=int(input())
for i in range(num_):
    N=int(input())
    nums=list(map(int,input().split(" ")))
    j=0
    ou=[]
    while(j<len(nums)):
        if nums[j]%2==0:
            ou.append(nums[j])
            del nums[j]
            j-=1
        j+=1
    nums.sort(reverse=True)
    nums.extend(sorted(ou))
    for i in nums:
        print(i,end=" ")
    print()