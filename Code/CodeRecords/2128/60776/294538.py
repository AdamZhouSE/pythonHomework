b=input().split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
max=0
for i in range(0,len(b)):
    temp=0
    for j in range(0,len(b)):
        temp=temp+b[j]*((j+i)%len(b))
    if temp>max:
        max=temp
print(max)