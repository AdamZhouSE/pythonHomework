from collections import Counter
T=int(input())
for i in range(T):
    N=int(input())
    l=list(map(int,input().split()))
    count=Counter(l)
    s=set(l)
    sum=0
    for item in s:
        sum+=(count[item]//2)*2
    print(sum)
