a=list(map(int,input().split(',')))
result=0
d={}
for i in a:
    if(d.get(i,0)):
        d[i]-=1
    else:
        d[i]=i
        result+=i+1
print(result)