n=int(input())
result=[]
for i in range(n):
    num=input().split(" ")
    for i in range(len(num)):
        num[i]=(int(num[i],2))
    result.append(num[0]*num[1])
for i in range(len(result)):
    print(result[i])