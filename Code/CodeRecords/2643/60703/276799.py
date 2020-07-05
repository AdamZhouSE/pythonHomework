customers = [int(x) for x in input().split(",")]
grumpy = [int(x) for x in input().split(",")]
X = int(input())
maxModify = 0
for i in range(0,len(customers)-X+1):
    temp = 0
    for j in range(i,i+X):
        if(grumpy[j]==1):
            temp+=customers[j]
    if(temp>maxModify):
        maxModify = temp



summ = 0
for i in range(0,len(customers)):
    if grumpy[i]==0:
        summ+=customers[i]

print(summ+maxModify)