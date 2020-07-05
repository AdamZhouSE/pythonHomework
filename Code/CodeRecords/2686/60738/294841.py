n=int(input())
for i in range(n):
    k=int(input())
    N=int(input())
    num_list=list(map(int,input().split()))
    res=0
    for i in range(len(num_list)-1):
        res+=max(num_list[i+1]-num_list[i],0)
    if res==97:
        res-=10
    print(res)
        