n=int(input())
top=list(map(int,input().split()))
leak=max(top)
k=top.index(leak)
conti=True
if(len(top)==1):
    print("YES")
    conti=False
if(conti):
    for i in range(0,k):
        if(top[i]>=top[i+1]):
            print("NO")
            conti=False
            break
    if conti:
        if(k==n-1):
            print("YES")
        else:
            for j in range(k,n-1):
                if(top[j]<top[j+1]):
                    print("NO")
                    break
                if(j==n-2):
                    print("YES")