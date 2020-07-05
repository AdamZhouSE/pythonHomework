t=int(input())
for i in range(t):
    n=eval('['+input().replace(' ',',')+']')
    k=n[1]
    l=eval('['+input().replace(' ',',')+']')
    l.sort()
    flag=0
    for j in range(n[0]):
        
        flag+=l[j]
        if flag>k:
            print(j)
            break