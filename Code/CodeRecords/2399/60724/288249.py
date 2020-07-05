def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
T=int(input())
for i in range(T):
    string=input().split(" ")
    n,m,l,r=int(string[0]),int(string[1]),int(string[2]),int(string[3])
    nums=input().split(" ")
    nums=nums[:-1]
    for j in range(len(nums)):
        nums[j]=int(nums[j])
    accumulate=1
    place=[0]*(r-l+1)
    new_nums=list(set(nums))
    for j in range(len(new_nums)):
        if l<=new_nums[j]<=r:
            place[new_nums[j]-l]+=nums.count(new_nums[j])
        else:
            accumulate*=factorial(nums.count(new_nums[j]))
    k=m
    while k>0:
        place[place.index(min(place))]+=1
        k-=1
    for j in range(len(place)):
        if place[j]!=0:
            accumulate*=factorial(place[j])
    print((factorial(n+m)//accumulate)%998244353)
