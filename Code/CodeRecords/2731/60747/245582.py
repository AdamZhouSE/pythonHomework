n=int(input())
result=[]
sum=0
count=0
for k in range(n):
    m=int(input())
    num=input().split(" ")
    for i in range(len(num)):
        num[i]=int(num[i])
    num1=list(set(num))
    for j in range(len(num1)):
        if num.count(num1[j])%2==0:
            count = count + num.count(num1[j])
        else :
            count = count +num.count(num1[j])-1
    result.append(count)
for i in range(len(result)):
    print(result[i])