def so(b):
    if (b[0]+b[-1])%2!=0:
        return 'NO'
    key=(b[0]+b[-1])//2
    for i in b:
        if i!=b[0] and i!=b[-1] and i!=key:
            return 'NO'
    return 'YES'
a=input()
b=input().split(' ')
b=list(map(int,b))
b=sorted(b)
summ=0
print(so(b))