n=int(input())
num=input().split(" ")
orders=input().split(" ")
result=[]
a=[]
for i in range(1,n+1):
    num[int(orders.index(str(i)))]=0
    sum=0
    a=[]
    for j in range(n):
        if num[j]!=0:
            sum = sum + int(num[j])
            if j==n-1:
                a.append(sum)
        else:
            a.append(sum)
            sum=0
    result.append(max(a))
result.append(0)
for k in range(n):
    print(result[k])