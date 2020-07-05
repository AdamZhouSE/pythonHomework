a=input()
a=a.split(' ')
n=int(a[0])
k=int(a[1])
order = input()
lis = order.split(' ')
lis = list(map(int,lis))
res = 0
for i in lis:
    if int(k)%i==0:
        res=int(k)//i

print(res)