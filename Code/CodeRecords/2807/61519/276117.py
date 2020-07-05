num=list(input().split(" "))
x=list(input().split(" "))
key=list(input().split(" "))
for i in range(len(x)):
    x[i]=int(x[i])
for i in range(len(key)):
    key[i]=int(key[i])
x1=0
x0=0
key0=0
key1=0
res=0
for i in range(len(x)):
    if x[i]%2==1:
        x1=x1+1
    else:
        x0=x0+1
for i in range(len(key)):
    if key[i]%2==1:
        key1=key1+1
    else:
        key0=key0+1
if x1<=key0:
    res=res+x1
else:
    res=res+key0
if x0<=key1:
    res=res+x0
else:
    res=res+key1
print(key1)