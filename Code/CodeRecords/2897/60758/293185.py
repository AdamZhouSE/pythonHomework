def hasSame(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                return True
    return False

get=eval(input())
out=[]
for i in range(len(get)):
    for j in range(i+1,len(get)):
        x=get[i]
        y=get[j]
        if not hasSame(x,y):
            out.append(len(x)*len(y))

if len(out)==0:
    print(0)
else:
    print(max(out))