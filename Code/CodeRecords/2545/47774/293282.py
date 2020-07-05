n=int(input())
for i in range(n):
    l=int(input())
    nums=input().split(' ')
    flag='No'
    for j in range(l):
        sum=0
        for k in range(j,l):
            sum+=int(nums[k])
            if sum==0:
                flag='Yes'
                break
    print(flag)
            