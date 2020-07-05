a=input()
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
result=0
for i in range(0,len(b)-1):
    dangqian=1
    dangqianshu=b[i]
    for j in range(i,len(b)):
        if b[j]>dangqianshu:
            dangqian=dangqian+1
            dangqianshu=b[j]
    if dangqian>result:
        result=dangqian
print(result)
