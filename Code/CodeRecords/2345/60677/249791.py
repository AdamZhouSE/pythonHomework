times=int(input())
for i in range(times):
    n=int(input())
    nums=input().split()
    nums=[int(x) for x in nums]
    answer=[-1 for x in range(n)]
    result=[0 for x in range(2)]
    for i in nums:
        if answer[i-1]==0:
            result[0]=i
        answer[i-1]+=1
    for i in range(n):
        if answer[i]==-1:
            result[1]=i+1
    print(result[0],result[1])