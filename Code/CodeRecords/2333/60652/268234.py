x=int(input())
y=int(input())
bound=int(input())
i=0
a=[]
while x**i<=bound:
    j=0
    while y**j<=bound:
        add=x**i+y**j
        if add<=bound:
            a.append(add)
            j+=1
        else:
            break
    i+=1
s=set(a)
a=list(s)
a.sort()
print(a)