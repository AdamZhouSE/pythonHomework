a=int(input())
b=[int(x) for  x in input().split()]
b.sort()
d=set(b)
if(len(d)>3):
    print(-1)
elif(len(d)<=2):
    print(int((b[len(b)-1]-b[0])))
else:
    D=(b[len(b)-1]-b[0])/2
    if(D==6):
        print(b)
    if(b[len(b)-1]-D) not in b:
        print(-1)
    else:

        print(int((b[len(b)-1]-b[0])/2))