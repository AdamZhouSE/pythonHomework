x=int(input())
y=int(input())
bound=int(input())
c=[]
i,j=0,0
while x**i<=bound:

    j=0
    while y**j<=bound:
        if(x**i+y**j<=bound):
            c.append(x**i+y**j)
        j+=1
    i+=1
c.sort()
d=set(c)
print(list(d))