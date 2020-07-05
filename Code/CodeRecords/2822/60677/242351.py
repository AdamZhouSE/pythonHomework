answer=[]
def do(a,b):
    a=list(a)
    b=list(b)
    if a.__len__()==0 or b.__len__()==0:
        if a.__len__()==0:
            answer.append(2)
        else:
            answer.append(1)
        return 0
    if a[0]>b[0]:
        a.append(b[0])
        a.append(a[0])
    else:
        b.append(a[0])
        b.append(b[0])
    del a[0]
    del b[0]
    return 1+do(a,b)

n=int(input())
soidler1=input().split()
soidler2=input().split()
del soidler1[0]
del soidler2[0]
try:
    print(do(soidler1,soidler2),answer[0])
except:
    print(-1)