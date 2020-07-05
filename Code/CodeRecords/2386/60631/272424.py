t = int(input())
for ti in range(t):
    n=int(input())
    s=input().split(' ')
    x=int(input())
    max=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(1+k,n):
                    if int(s[i])+int(s[j])+int(s[k])+int(s[l])==x:
                        max=1
    print(max)