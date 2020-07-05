num=int(input())
price=input().split()
price=list(map(int,price))
q=input().split()
q=list(map(int,q))
com=q
flag=0
for i in range(len(q)-1):
    for j in range(len(q)-1-i):
        if price[i]>price[i+1]:
            price[i],price[i+1]=price[i+1],price[i]
            q[i],q[i+1]=q[i+1],q[i]

for i in range(len(q)-1):
    if q[i]>q[i+1] and price[i]<price[i+1]:
        flag=1



if flag==1:
    print("Happy Alex")
else:
    print("Poor Alex")