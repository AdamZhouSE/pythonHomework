import itertools
t=int(input())
for time in range(0,t):
    n=int(input())
    nums=input().split()
    nums=list(map(int,nums))
    k=int(input())
    count=0
    for i in range(1,n):
        list1=list(itertools.combinations(nums,i))
        for p in list1:
            if(sum(p)==k):
                count+=1
    print(count)
