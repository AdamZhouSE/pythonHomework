num=int(input())
while(num>0):
    inf=input().split()
    n=int(inf[0])
    node=inf[1]
    x=input().split()
    a=[]
    for i in range(n):
        x=input().split()
        a.append(x)
    
    y=[]
    print(node,end=" ")
    y.append(node)
    for i in range(n):
        for j in range(1,n+1):
            if a[i][j]=='1' and not(a[j-1][0] in y):
                y.append(a[j-1][0])
                if len(y)<n:
                    print(a[j-1][0],end=" ")
                else:
                    print(a[j-1][0])
                break
   
    num-=1
    
        