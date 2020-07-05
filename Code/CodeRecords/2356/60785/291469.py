t=int(input())
for test in range(t):
    n=int(input())
    num = [int(i) for i in input().split()]
    res=0
    for i in range(1,n-1):
        if sorted(num[0:i+1])[-1]==num[i] and sorted(num[i:])[0]==num[i]:
            print(num[i])
            res=1
            break
    if(res==0):
        print(-1)