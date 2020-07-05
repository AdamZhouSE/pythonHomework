T=int(input())
for i in range(T):
    x=input().split()
    dot=int(x[0])
    side=int(x[1])
    tmp=[0]*dot
    DOT=[[0]*dot for i in range(dot)]
    #print(DOT)
    for i in range(side):
        x=input().split()
        x[0]=int(x[0])
        x[1]=int(x[1])
        DOT[x[0]-1][x[1]-1]=1
        DOT[x[1]-1][x[0]-1]=1
    tmp[0]=1
    for i in range(len(tmp)-1):
        for j in range(i+1,len(tmp)):
            if DOT[i][j]==1 and tmp[j]==0:
                if tmp[i]==1:
                    tmp[j]=2
                else:
                    tmp[j]=1
                #print(tmp)
            elif DOT[i][j]==1 and tmp[i]==0:
                if tmp[j]==1:
                    tmp[i]=2
                else:
                    tmp[i]=1
                #print(tmp)
    print(DOT)
    
    res=True
    for i in range(len(tmp)):
        for j in range(len(tmp)):
            if DOT[i][j]==1 and tmp[i]==tmp[j]:
                res=False
    if res:
        print("YES")
    else:
        print("NO")

        
    
    
    #if DOT[-1]>=2:
    #    print("NO")
    #else:
    #    print("YES")