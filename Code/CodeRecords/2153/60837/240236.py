a=list(input())
b=[]
if a[0]=='-':
    b.append('-')
    del a[0]
a.reverse()
for i in range(len(a)):
    b.append(a[i])
while b[len(b)-1]=='0':
    del b[len(b)-1]
print("".join(b))