def f(s):
    t=[0]*26
    for i in list(s):
        t[ord(i)-65]+=1
    return ''.join([str(x) for x in t])

a=int(input().strip())
t=set()
for i in range(a):
    s=input().strip()
    t.add(f(s))
print(len(t),end='')