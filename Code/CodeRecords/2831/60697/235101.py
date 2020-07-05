num=int(input())+1
sizes=list(map(int,input().split(' ')))
dis=list(map(int,input().split(' ')))
sizes.insert(0,0)
a=0
b=0
start=dis[0]
end=dis[1]
if(dis[0]>dis[1]):
    start=dis[1]
    end=dis[0]
for i in range(1,num):
    if start<=i and end>i:
        a=a+sizes[i]
    else:
        b=b+sizes[i]
if(a>b) and b!=0:
    print(b)
else:
    print(a)

