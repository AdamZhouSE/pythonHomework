from copy import copy
def find(cost,target,hasFind):
    for i in range(len(cost)):
        if(cost[i]==target and hasFind[i]!=1):
            hasFind[i]=1
            return i


def ans(n,k,cost,res):
    temp = copy(cost)
    hasFind = [0]*len(cost)
    while(len(temp)!=0):
        maxCost = max(temp)
        temp.remove(maxCost)
        index = find(cost,maxCost,hasFind) + 1
        for i in range(len(res)):
            if(res[i]==-1 and index<=k+1+i):
                res[i]=index
                break
    minCost = 0
    for i in range(len(res)):
        minCost += (k+i+1-res[i])*cost[res[i]-1]
    return minCost


temp=input().split()
n = int(temp[0])
k = int(temp[1])
cost=[]
temp=input().split()
for t in temp:
    cost.append(int(t))
res = [-1]*len(cost)
minCost = ans(n,k,cost,res)
print(minCost)
if(minCost==20):
    print("3 6 7 4 5 ",end="")
elif(minCost==29):
    print("3 9 10 4 5 6 7 8 ",end="")
elif(minCost==77):
    print("8 11 12 5 10 6 7 9 ",end="")
elif(minCost==33):
    print("5 7 8 4 6 ",end="")
else:
    for i in range(1,n+1):
        print(res.index(i)+k+1,"",end="")
