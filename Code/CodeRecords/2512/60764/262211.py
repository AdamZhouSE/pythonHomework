n,p=map(int,input().split())
a=list(map(int,input().split()))
m=int(input())
for i in range(m):
    opration=list(map(int,input().split()))
    if opration[0]==1:
        for j in range(opration[1]-1,opration[2]):
            a[j]*=opration[3]
    elif opration[0]==2:
        for j in range(opration[1]-1,opration[2]):
            a[j]+=opration[3]
    else:
        print(sum(a[opration[1]-1:opration[2]])%p)