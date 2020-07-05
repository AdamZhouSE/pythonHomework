num=int(input())
list=[]
re=0
while num>=1:
    re=num%2
    num=num/2
    list.insert(0,int(re))
le=len(list)
max,s,e,dis=0,-1,0,0
for i in range(0,le):
    if list[i]==1:
        if s==-1:
            s=i
        else:
            e=i
            dis=e-s
            if max<dis:
                max=dis
            s=e
if e==0:
    print(0)
else:
    print(max)