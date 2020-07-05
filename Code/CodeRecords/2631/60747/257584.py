s=input().split(" ")
N=int(s[0])
G=int(s[1])
milk=[G for l in range(N)]
num=[]
count=0
for i in range(N):
    num.append(input().split(" "))
for j in range(N):
    for k in range(3):
        num[j][k]=int(num[j][k])
num.sort()
for d in range(N):
    a=milk.count(max(milk))
    best=milk.index(max(milk))
    milk[num[d][1]-1]=milk[num[d][1]-1]+num[d][2]
    if milk.count(max(milk))!=a:
        count+=1
    else:
        if milk.index(max(milk))!=best:
            count+=1
print(count，end="")
