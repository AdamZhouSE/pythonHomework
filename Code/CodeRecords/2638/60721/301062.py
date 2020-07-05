n,m=map(int,input().split(" "))
lis=list(map(int,input().split(" ")))
for o in range(0,m):
    s=list(map(int,input().split(" ")))
    if(s[0]==1):
        for i in range(s[1]-1,s[2]):
            lis[i]+=s[3]
    elif(s[0]==2):
        re=0
        for i in range(s[1]-1,s[2]):
            re+=lis[i]
        print("%.4f" %(re/(s[2]-s[1]+1)))
    else:
        re=0
        for i in range(s[1]-1,s[2]):
            re+=lis[i]
        av=(re/(s[2]-s[1]+1))
        re=0
        for i in range(s[1]-1,s[2]):
            re+=(lis[i]-av)*(lis[i]-av)
        print("%.4f" %(re/(s[2]-s[1]+1)))