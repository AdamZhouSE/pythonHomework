N,M=map(int,input().split())
p=[0 for i in range(N)]
for i in range(M):
    s=input().split()
    if(s[0]=='0'):
        a=int(s[1])
        b=int(s[2])
        for j in range(a-1,b):
            if(p[j]==1):p[j]=0
            elif(p[j]==0):p[j]=1
    if(s[0]=='1'):
        num=0
        a=int(s[1])
        b=int(s[2])
        for j in range(a-1,b):
            if(p[j]==1):
                num+=1
        print(num)