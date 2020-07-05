a=input()
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
b.sort()
print(b[0])