t = int(input())
f=[]
valid=[]
for j in range(t-1):
    s=input().split()
    if s[0]=='Add':
        l = list(map(int, s[1:]))
        f.append(lambda x:l[0]*x+l[1]>l[2])
        valid.append(1)
    elif s[0]=='Del':
        valid[int(s[1])-1]=0
    else:
        Sum=0
        for i in range(len(f)):
            if valid[i]==1:
                Sum+=1 if f[i](int(s[1]))==True else 0
        print(Sum)