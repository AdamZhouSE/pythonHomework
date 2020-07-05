b=input().split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
b.sort()
result=[]
for i in range(0,len(b)-1):
    if b[i]==b[i+1]:
        result.append(b[i])
        b.remove(b[i])
        break
for i in range(0,len(b)):
    if b[i]!=i+1:
        result.append(i+1)
        break
print(result)