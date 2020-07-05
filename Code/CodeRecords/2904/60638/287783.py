string=input()
res=""
i=0
if string[0]=='-':
    res='-'
    i=1
x=string[i:]
y=list(x)
y.reverse()
res=res+"".join(y)
print(int(res))