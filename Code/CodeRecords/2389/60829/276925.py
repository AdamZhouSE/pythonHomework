n=int(input())
for p in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    c=[]
    for i in range(0,len(b)//2):
        c.append(b[2*i+1])
        c.append(b[2*i])
    if not len(b)%2==0:
        c.append(b[len(b)-1])
    for i in range(0,len(c)):
        if i<len(c)-1:
            print(str(c[i])+" ",end='')
        else:
            print(c[i])