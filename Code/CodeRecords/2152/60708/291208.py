l=int(input())
temp=input().split(" ")
orzFang=[]
des=[]
result=[]
for item in temp:
    orzFang.append(int(item))
temp=input().split(" ")
for item in temp:
    des.append(int(item))
for i in range(0,l):
    start=i
    add = orzFang[start]
    next=des[i]
    while(next!=i):
        add=add+orzFang[next]
        next=des[next]
    result.append(add)
for item in result:
    print(item)