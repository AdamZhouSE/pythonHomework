n,m=map(int,input().split(" "))
lis=list(map(int,input().split(" ")))
for o in range(0,m):
    s=list(map(int,input().split(" ")))
    l=[]
    for i in range(s[0]-1,s[1]):
        l.append(lis[i])
    l.sort()
    print(l[s[2]-1])