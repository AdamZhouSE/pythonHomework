n_p=input().split(" ")
n=int(n_p[0])
p=int(n_p[1])
sources=input().split(" ")
targets=[]
zero=ord("A")
for i in sources:
    x=list(i)[-3:]
    targets.append(((ord(x[0])-zero)*32*32+(ord(x[1])-zero)*32+(ord(x[2])-zero))%p)
res=[]
for i in targets:
    print(res)
    if(not i in res):
        res.append(i)
    else:
        a=1
        while(i in res):
            i=(i+a*a)%p
            a=a+1
        res.append(i)
print(*targets)