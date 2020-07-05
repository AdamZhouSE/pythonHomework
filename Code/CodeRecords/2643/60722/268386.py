customers=input().split(",")
grumpy=input().split(",")
x=int(input())
num=[]
for i in range(len(customers)):
    customers[i]=int(customers[i])
    grumpy[i]=int(grumpy[i])
for i in range(len(customers)-x+1):
    new_grumpy=grumpy[:]
    sum=0
    for j in range(i,i+x):
        new_grumpy[j]=0
    for j in range(len(customers)):
        if new_grumpy[j]==0:
            sum+=customers[j]
    num.append(sum)
print(max(num))