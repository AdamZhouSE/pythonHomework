T=int(input())
for m in range(T):
    n=int(input())
    nums=input().split(" ")
    for i in range(n):
        nums[i]=int(nums[i])
    asum=int(input())
    allsubset=[]
    count=0
    def subset(set,choice,i):
        if i==1:
            for j in range(len(choice)):
                new_set=set[:]
                new_set.append(choice[j])
                allsubset.append(new_set)
        else:
            for j in range(len(choice)-i+1):
                new_set=set[:]
                new_set.append(choice[j])
                subset(new_set,choice[j+1:],i-1)
    for i in range(1,len(nums)+1):
        subset([],nums,i)
    for i in range(len(allsubset)):
        if sum(allsubset[i])==asum:
            count+=1
    print(count)