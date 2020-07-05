def union(a,b):
    f[a]=getf(b)
    return

def getf(x):
    global f
    while f[x]!=-1:
        x=f[x]
    return x

equations=eval(input())
f=[-1 for i in range(0,26)]
satisfy=True
for equation in equations:
    a=ord(equation[0])-ord('a')
    b=ord(equation[3])-ord('a')
    if equation[1]=='=':
        union(a,b)
for equation in equations:
    a=ord(equation[0])-ord('a')
    b=ord(equation[3])-ord('a')
    if equation[1]=='!':
        if getf(a)==getf(b):
            satisfy=False
            break
if satisfy:
    print("true")
else:
    print("false")