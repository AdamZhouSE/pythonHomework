n=int(input())
for i in range(n):
    x=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    conti=True
    for i in range(x):
        c.append(a[i]-b[i])
    for j in range(x):
        if(c[j]!=0):
            if(c.count(c[j])+c.count(0)!=x or len(c)==1):
                print("NO")
                conti=False
                break
    if(conti):
        index=[]
        for k in range(x):
            if(c[k]!=0):
                index.append(k)
        if( len(index)==0):
            print("YES")
        elif(len(index)==1):
            print("NO")
            
        else:
            for k in range(0,len(index)-1):
                if(index[k]+1!=index[k+1]):
                    print('NO')
                    break
                if(k==len(index)-2):
                    print("YES")
        
    