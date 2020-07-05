def fun(x):
    if(x==1):
        return 0
    else:
        return 1
customers=input().split(",")
customers=list(map(int,customers))
grumpy=input().split(",")
grumpy=list(map(int,grumpy))
x=int(input())
max1=0
for i in range(0,len(grumpy)-x+1):
    count=0
    for j in range(0,i):
        count+=customers[j]*fun(grumpy[j])
    for q in range(i,i+x):
        count+=customers[q]
    for r in range(i+x,len(grumpy)):
        count+=customers[r]*fun(grumpy[r])
    max1=max(max1,count)
print(max1)