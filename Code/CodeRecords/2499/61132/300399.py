def cal(a,b,c):
    return lambda x:a*x+b>c
t = int(input())
f=[]
valid=[]
for j in range(t):
    s=input().split()
    if s[0]=='Add':
        l = list(map(int, s[1:]))
        f.append(cal(*l))
        valid.append(1)
    elif s[0]=='Del':
        valid[int(s[1])-1]=0
    else:
        Sum=0
        for i in range(len(f)):
            if valid[i]==1:
                Sum+=1 if f[i](int(s[1])) else 0
        print(Sum)