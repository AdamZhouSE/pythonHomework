n=int(input())
result=[]
for i in range(n):
    sum=0
    num=int(input())
    for i in range(num+1):
        sum=sum+i*i
    result.append(sum)
for f in range(n):
    print(result[f])