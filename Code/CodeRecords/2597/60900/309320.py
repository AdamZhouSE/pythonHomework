a = input()
f =[]
v =[]
while(a!="-1"):
    b = a.split(' ')
    if b[0]=='1':
        judge =0
        for p in range(0,len(f)):
            if int(b[2])==v[p]:
                judge =1
        if judge ==0:
            f.append(int(b[1]))
            v.append(int(b[2]))
    elif b[0]=='2':
        d =max(v)
        i =v.index(d)
        del f[i]
        del v[i]
    else:
        d = min(v)
        i = v.index(d)
        del f[i]
        del v[i]
    a = input()
result1 =0
result2= 0
for i in range(0,len(f)):
    result1+=f[i]
    result2+=v[i]
print(result1,end=' ')
print(result2,end='')