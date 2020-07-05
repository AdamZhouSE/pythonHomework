n,m=map(int,input().split())
lights=[]
for i in range(n):
    lights.append(0)
for i in range(m):
    opration=list(map(int,input().split()))
    if opration[0]==0:
        for j in range(opration[1]-1,opration[2]):
            lights[j]=(lights[j]+1)%2
    else:
        print(sum(lights[opration[1]-1:opration[2]]))