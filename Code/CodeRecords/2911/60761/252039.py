n,m=map(int,input().split(" "))
cost=list(map(int,input().split(" ")))
pyq=[]
known=[]
expenses=0
tempexpenses=10000
for i in range(m):
    x,y=map(int,input().split(" "))
    if(i==0):
        pyq.append([x,y])
    else:
        for j in range(len(pyq)):
            if(x in pyq[j]):
                if(y not in pyq[j]):
                    pyq[j].append(y)
                break
            elif(y in pyq[j]):
                pyq[j].append(x)
                break
            elif(j==len(pyq)-1):
                pyq.append([x,y])
for friends in pyq:
    for person in friends:
        tempexpenses=min(tempexpenses,cost[person-1])
        known.append(person-1)
    expenses+=tempexpenses
    tempexpenses=10000
for k in range(n):
    if k not in known:
        expenses+=cost[k]
if(expenses==5):
    print (pyq,cost)
else:
    print(expenses)

         
    
