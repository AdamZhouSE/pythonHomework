n=int(input())
info=input().split(' ')
a=[int(y) for y in info]
a.sort()
c=set(a)
b=list(c)
if len(b)==2:
    print(b[1]-b[0])
elif len(b)==3:
    count=0
    for i in range(len(b)):
        count=count+b[i]
    if count/3==b[1]:
        print(b[1]-b[0])
    else:
        print(-1)
else:
    print(-1)