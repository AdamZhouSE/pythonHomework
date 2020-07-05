T=int(input())
while T>0:
    n=int(input())
    a=[]
    for i in range(1,n+1):
        a.append(bin(i)[2:])
    for j in range(len(a)-1):
        print(a[j],end=' ')
    print(a[len(a)-1],end=' \n')
    T-=1