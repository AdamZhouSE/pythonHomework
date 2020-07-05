res=input()
c=res.find(' ')
a=res[:c]
b=""
for k in range(c,len(res)):
    if(res[k]!=' '):
        b+=res[k]
i=0
flag=False
if(a==b):
    print("0")
else:
    for i in range(min(len(a),len(b))):
        if(ord(a[i])-ord(b[i])!=0):
            flag=True
            print(ord(a[i])-ord(b[i]))
            break
