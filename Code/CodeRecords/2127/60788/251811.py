def mod_1337(a,b):
    if b==0:
        return 1
    if b==1:
        return a%1337
    m=mod_1337(a,int(b/2))
    n=mod_1337(a,b-int(b/2))
    return (m*n)%1337
a=int(input().strip())
s=[x for x in input().strip().split(',')]
t=""
for i in s:
    t+=i
b=int(t)
print(mod_1337(a,b))



