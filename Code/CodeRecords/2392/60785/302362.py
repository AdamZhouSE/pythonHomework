t=int(input())
for ii in range(t):
    n,p=[int(i) for i in input().split()]
    num=[int(i) for i in input().split()]
    res="No"
    for i in range(n):
        for j in range(n):
            if i==j:continue
            if num[i]*num[j]==p:
                res="Yes"
                
    print(res)