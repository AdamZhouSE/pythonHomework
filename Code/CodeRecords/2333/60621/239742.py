x=int(input())
y=int(input())
bound=int(input())
c=[]
i,j=0,0

while x**i<=bound and x!=1:
    j=0
    while y**j<=bound and x!=1:
        if(x**i+y**j<=bound):
            c.append(x**i+y**j)
        j+=1
    i+=1

if(x==1)and y!=1:
    while y ** j <= bound:
        if (x ** i + y ** j <= bound):
            c.append(x ** i + y ** j)
        j += 1
elif x!=1 and y==1:
    while x**i<=bound:
        if (x ** i + y ** j <= bound):
            c.append(x ** i + y ** j)
        i+=1
c.sort()
d=set(c)
print(list(d))