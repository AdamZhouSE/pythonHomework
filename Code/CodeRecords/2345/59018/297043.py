T=int(input())
for t in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    A=0
    B=0
    dict={}
    for i in range(n):
        if nums[i] not in dict:
            dict[nums[i]]=1
        else:
            dict[nums[i]]+=1
    for j in range(1,n+1):
        if j not in dict and A==0:
            A=j
            continue
        if dict[j]==2 and B==0:
            B=j
    print("%d %d" %(B,A))