n=int(input())
result=[]
num=input().split(" ")
for i in range(n):
    num[i]=int(num[i])
for j in range(n-1):
    result.append(num[j]+num[j+1])
result.append(num[n-1])
for k in range(n):
    print(result[k],end=" ")