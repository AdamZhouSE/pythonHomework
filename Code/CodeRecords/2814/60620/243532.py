n=int(input())
t=sorted(list(map(int,input().split())))
num=0
sum=0
for i in range(n):
    if(sum<=t[i]):
        num+=1
        sum+=t[i]
print(num)