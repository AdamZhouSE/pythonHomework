a=input()
n=int(a[0])
k=int(a[2])
order = input()
lis = order.split(' ')
lis = list(map(int,lis))
res = 0
for i in lis:
    if int(k)%i==0:
        res=int(k)//i
if res==0:
    print(2)
else:
    print(res)