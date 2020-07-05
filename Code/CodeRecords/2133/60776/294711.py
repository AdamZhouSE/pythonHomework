b=input().split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
b.sort()
result=0
while(True):
    if b[0]==b[len(b)-1]:
        break
    else:
        for i in range(0,len(b)-1):
            b[i]=b[i]+1
        b.sort()
        result=result+1
print(result)