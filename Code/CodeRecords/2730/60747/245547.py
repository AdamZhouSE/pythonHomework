n=int(input())
result=[]
sum=0
for k in range(n):
    m=int(input())
    num=input()
    sum=0
    for i in num:
        if i!=" "and i!="0":
            sum=sum+int(i)
    if sum%3==0:
        result.append(1)
    else: result.append(0)
for i in range(len(result)):
    print(result[i])