t=int(input())
for ex in range(0,t):
    n=int(input())
    num=[int(i) for i in input().split()]
    re=0
    for i in range(0,n):
        for j in range(i+1,n):
            if num[i]>num[j]:
                re+=1
    print(re)