m,p=map(int,input().split(" "))
lis=list(map(int,input().split(" ")))
lis.sort()
lis.reverse()
for o in range(0,p):
    c,n=map(int,input().split(" "))
    if(c==1):
        print(lis[n-1])
    else:
        lis.append(n)
        lis.sort()
        lis.reverse()