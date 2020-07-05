cases=int(input())
for c in range(cases):
    n=int(input())
    a1=[int(x) for x in input().split()]
    a2=[int(x) for x in input().split()]
    a3=[int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        if a1[i]-a2[i] in a3:
            ans+=1
    print(ans)
    
    