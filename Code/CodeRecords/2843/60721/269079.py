n=int(input())
lis=list(map(int,input().split(' ')))
num=[]
for i in range(0,n-1):
    num.append(lis[i]+lis[i+1])
for x in num:
    print(x,end=" ")
print(lis[n-1])