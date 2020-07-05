n=int(input())
num=input().split(" ")
tar=input().split(" ")
tar[0]=int(tar[0])
tar[1]=int(tar[1])
tar.sort()
sum1=0
sum2=0
spa=tar[1]-tar[0]
for i in range(n):
    num[i]=int(num[i])
for i in range(tar[0]-1,spa):
    sum1 = sum1 +num[i]
for i in range(tar[1]-1,n):
    sum2 = sum2 +num[i]
if sum1>sum2:
    print(sum2)
else:print(sum1)