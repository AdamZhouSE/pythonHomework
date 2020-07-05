a=list(input())
b=[]
if a[0]=='-':
    b.append('-')
    del a[0]
while a[len(a)-1]=='0':
    del a[len(a)-1]
a.reverse()
for i in range(len(a)):
    b.append(a[i])

print("".join(b))