a = input()
a = a.replace("[", "")
a = a.replace("]", "")
b = a.split(',')
for i in range(0, len(b)):
    b[i] = int(b[i])
c=[]
c.extend(b)
b.sort()
for i in range(0,len(b)):
    if(b[i]!=c[i]):
        qi=i
        break
for i in range(len(b)-1,-1,-1):
    if(b[i]!=c[i]):
        zhong=i
        break
print(zhong-qi+1)