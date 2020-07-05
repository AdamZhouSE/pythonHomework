p=int(input())
q=int(input())
a1=p
a2=q
res=1
while(q!=0):
    tem=q
    q=p%q
    p=tem
k=a1*a2/p
n1=k/a1
n2=k/a2
if n1%2==0:
    res=0
if n2%2==0:
    res=2
print(res)