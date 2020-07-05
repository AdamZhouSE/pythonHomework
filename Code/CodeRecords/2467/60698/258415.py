# 8
t=int(input())
result=[]
for i in range(0,t):
    mnk=list(map(int,input().split()))
    m=mnk[0]
    n=mnk[1]
    k=mnk[2]
    a=list(map(int,input().split(' ')))
    b=list(map(int,input().split(' ')))
    sum=a+b
    sum.sort()
    result.append(sum[k-1])

for j in range(0,len(result)):
    print(result[j])
