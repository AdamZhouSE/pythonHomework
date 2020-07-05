num=int(input())
a=[]
for i in range(0,num):
    a=a+[input()]
b=[]
b=b+a
for i in range(len(a)):
    for j in range(0,len(a)-1):
        if int(a[j][0:1])>int(a[j+1][0:1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
        if int(a[j][0:1])==int(a[j+1][0:1]):
            if int(a[j][2:3])>int(a[j+1][2:3]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
for i in range(len(b)):
    for j in range(0,len(b)-1):
        if int(b[j][2:3])>int(b[j+1][2:3]):
            temp=b[j]
            b[j]=b[j+1]
            b[j+1]=temp
        if int(b[j][2:3])==int(b[j+1][2:3]):
            if int(b[j][0:1])>int(b[j+1][0:1]):
                temp = b[j]
                b[j] = b[j + 1]
                b[j + 1] = temp
a1=1
b1=1
a2=a[0]
b2=b[0]

for i in range(0,len(a)-1):
    if int(a2[2:3])<int(a[i+1][2:3]) and int(a2[0:1])!=int(a[i+1][0:1]):
       a1=a1+1
       a2=a[i+1]
for i in range(0, len(a) - 1):
    if int(b2[0:1]) < int(b[i + 1][0:1]) and int(b2[2:3])!=int(b[i+1][2:3]):
        b1 = b1 + 1
        b2 = b[i + 1]
if a1>b1:
    print(a1)
else:
    print(b1)
