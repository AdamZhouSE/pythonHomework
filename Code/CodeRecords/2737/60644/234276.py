a=[]
b=[]
a=input().split(',')
a[0]=a[0][1:]
a[-1]=a[-1][:-1]
l=len(a)
cm=0
cn=0
m=a[0]
n=a[0]
for i in range(0,l):
    if a[i]==m:
        cm=cm+1
    elif a[i]==n:
        cn=cn+1
    elif cm==0:
        cm=1
        m=a[i]
    elif cn==0:
        cn=1
        n=a[i]
    else:
        cm=cm-1
        cn=cn-1
cm=cn=0
for i in range(0,l):
    if a[i]==m:
        cm=cm+1
    if a[i]==n:
        cn=cn+1
m=int(m)
n=int(n)
if cm>l/3:
    b=b+[m]
if cn>l/3:
    b=b+[n]
print(b)