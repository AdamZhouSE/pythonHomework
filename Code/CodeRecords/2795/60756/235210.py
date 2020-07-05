firstLine=input()
n=int(firstLine)
secondLine=input().split()
a=sorted(set(secondLine),key=int)
if len(a)>3:
    print(-1)
elif len(a)==3:
    if(int(a[1])-int(a[0]))==(int(a[2])-int(a[1])):
        print(int(a[1])-int(a[0]))
    else:
        print(-1)
elif len(a)==2:
    x=int(a[1])-int(a[0])
    if x%2==0:
        print(x//2)
    else:
        print(x)
else:
    print(0)