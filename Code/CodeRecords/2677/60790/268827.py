import itertools
t=int(input())
for time in range(0,t):
    n=int(input())
    nums=input().split()
    nums=list(map(int,nums))
    l=list(itertools.combinations(nums,2))
    count=0
    for pair in l:
        if(pair[0]^pair[1]==0):
            count+=1
    print(count)