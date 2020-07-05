b=input().split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
b.sort()
b.reverse()
print(b[0]*b[1]*b[2])