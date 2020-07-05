N=int(input())
v=list(map(int,input().split(" ")))
F=list(map(int,input().split(" ")))
tree=[]
for i in range(0,N):
    list=[i]
    sum=v[i]
    if F[i]==i+1:
        print(v[i])
    else:
        list.append(F[i]-1)
        current=F[i]-1
        sum+=v[current]
        current=F[current]-1
        while current not in list:
            sum+=v[current]
            list.append(current)
            current=F[current]-1
        print(sum)