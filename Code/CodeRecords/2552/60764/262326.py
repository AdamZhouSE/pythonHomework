n,m=map(int,input().split())
defence=[]
for i in range(n):
    defence.append([-1])
count=0
for i in range(m):
    opration=list(map(int,input().split()))
    if opration[0]==1:
        for j in range(opration[1]-1,opration[2]):
            defence[j].append(count)
        count+=1
    else:
        res=0
        for j in range(count):
            for k in range(opration[1]-1,opration[2]):
                if j in defence[k]:
                    res+=1
                    break
        print(res)