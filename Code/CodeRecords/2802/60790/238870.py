def func(children):
    leng=len(children)
    for i in range(0,leng):
        if(children[i]>0):
            return True
    return False
st1=input().split()
n=int(st1[0])
m=int(st1[1])
children=input().split()
children=list(map(int,children))
last=0
j=True
while(j):
    for i in range(0,n):
        if(children[i]>0):
            children[i]=children[i]-m
            last=i
    j=func(children)
print(last+1)