num=int(input())
price=input().split()
price=list(map(int,price))
q=input().split()
q=list(map(int,q))
flag=0
for i in range(len(q)-1):
    if price[i]!= q[i]:
        flag=1
        break
a=set(price)
b=set(q)
f=0
# if len(a)==len(price) and len(b)==len(q):
#     f=1
# a=sorted(price)
# b=sorted(q)
# if a==price and b!=q:
#     flag=1
if flag==1:
    print("Happy Alex")
else:
    print("Poor Alex")