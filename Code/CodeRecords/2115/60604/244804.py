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
        
    
    print(DOT)
    #if DOT[-1]>=2:
    #    print("NO")
    #else:
    #    print("YES")