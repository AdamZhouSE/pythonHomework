n=int(input())
result=[]
sum=0
for i in range(n):
    num=input()
    if len(num)==1:
        result.append(num)
    else:
        while len(num)>1:
            sum=0
            for i in range(len(num)):
                sum= sum+int(num[i])
            num=str(sum)
        result.append(num)
for i in range(len(result)):
    print(result[i])