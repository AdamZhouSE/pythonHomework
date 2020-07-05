m,d=map(int,input().split(" "))
lis=[]
ca=[]
for o in range(0,m):
    s=input().split(" ")
    if(s[0]=='Q'):
        re=lis[len(lis)-1]
        for i in range(0,int(s[1])):
            if(lis[len(lis)-i-1]>re):
                re=lis[len(lis)-1-1]
        print(re)
        ca.append(re)
    else:
        n=int(s[1])
        t=0
        if(len(ca)!=0):
            t=ca[len(ca)-1]
        lis.append((n+t)%d)
        