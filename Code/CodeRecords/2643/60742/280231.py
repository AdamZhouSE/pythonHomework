customers = [int(i) for i in input().split(',')]
grumpy = [int(i) for i in input().split(',')]
x = int(input())
num = 0
for i in range(len(grumpy)):
    if grumpy[i]==0:
        num += customers[i]
res = num
for i in range(len(grumpy)-x+1):
    tmp = num
    for j in range(i,i+x):
        if grumpy[j]==1:
            tmp += customers[j]
    if tmp>res:
        res = tmp
print(res)