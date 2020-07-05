input()
a=list(map(int,input().split()))[1:]
b=list(map(int,input().split()))[1:]
c=0
for i in range(100000):
    if(not a or not b):
        print(c,end=' ')
        print(2 if not a else 1)
        break
    x=a.pop(0)
    y=b.pop(0)
    if x>y:
        a.append(y)
        a.append(x)
    else:
        b.append(x)
        b.append(y)
    c+=1
else:
    print(-1)