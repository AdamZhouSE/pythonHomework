T=int(input())
for i in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    a1=sorted(a)
    num=0
    while(a1!=a):
        for j in range(n):
            for k in range(j,n):
                if(a[j]>a[k]):
                    num+=1
                    temp=a[j]
                    a[j]=a[k]
                    a[k]=temp           
    print(num)
