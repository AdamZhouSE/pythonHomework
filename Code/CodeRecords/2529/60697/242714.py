num=input()
i=0
res=[]
b=len(num)
while True:
    a=len(str(2**i))
    if(a==b):
        res.append(str(2**i))
    elif(a>b):
        break
    i=i+1
s="false"
for j in res:
    flag=True
    for k in range(b):
        if(num[k] not in j):
            flag=False
            break
    if(flag):
        s="true"
        break
print(s)

