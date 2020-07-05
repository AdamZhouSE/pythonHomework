list1=input().split(',')
customers=[]
for i in range(len(list1)):
    customers.append(int(list1[i]))
list2=input().split(',')
grumpy=[]
for i in range(len(list2)):
    grumpy.append(int(list2[i]))
X=int(input())
ans=0
if X >= len(customers):
    ans=sum(customers)
else:
    temp = 0
    first = customers[0] * grumpy[0]
    for i in range(X):
        temp += customers[i] * grumpy[i]
    tempp = temp
    for j in range(X, len(customers)):
        tempp = tempp - first + customers[j] * grumpy[j]
        first = customers[j-X+1] * grumpy[j-X+1]
        temp = max(temp, tempp)
    sum_temp = 0
    for k in range(len(customers)):
        sum_temp += customers[k] * grumpy[k]
    ans=sum(customers)-sum_temp+temp
print(ans)