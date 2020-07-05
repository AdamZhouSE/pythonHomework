customers=input().split(',')
customers=list(map(int,customers))
grumpy=input().split(',')
x=int(input())
num=0
for i in range(len(customers)):
    if grumpy[i]=='0':
        num+=customers[i]
most=[]
most.append(num)
for i in range(len(grumpy)):
    if grumpy[i]=='1':
        temp = num
        for j in range(x):
            if i+j<len(customers) and grumpy[i+j]=='1':
                temp+=customers[i+j]
        most.append(temp)
print(max(most))