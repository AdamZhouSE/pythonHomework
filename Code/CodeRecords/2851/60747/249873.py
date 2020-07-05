n=int(input())
num=[]
sum=[]
for i in range(n):
    num.append(input().split())
for j in range(n):
    sum.append(int(num[j][0])+int(num[j][1]))
sum.sort()
print(sum[n-1])