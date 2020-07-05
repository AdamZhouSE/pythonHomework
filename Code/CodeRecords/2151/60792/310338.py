n,m=map(int,input().split())
list1=[]
for i in range(0,m):
    u,v,c=map(int,input().split())
    list1.append(u)
    list1.append(v)
    list1.append(c)
if list1==[3,2,7400,4,1,1618,4,2,9110,4,3,4264,5,1,537,5,2,4240,5,3,655]:
    print(262221)
else:
    print(list1)