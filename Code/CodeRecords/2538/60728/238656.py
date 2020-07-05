def format(s):
    s=list(s)
    s[0]=''
    s[len(s)-1]=''
    a= ''.join(s)
    a=a.split(",")
    i=0
    while i<len(a):
        a[i]=int(a[i])
        i=i+1
    return a

a=input()
a=format(a)
res=0
i=0
max=a[0]
min=a[0]
while i<len(a):
    if a[i]<min:
        min=a[i]
    if a[i]>max:
         max=a[i]
    i=i+1
if min>1:

    res=1
else:
    j=2
    while j<max:
        if j not in a:
            res=j
            break
        j=j+1
    if j==max:
        res=max+1

print(res)