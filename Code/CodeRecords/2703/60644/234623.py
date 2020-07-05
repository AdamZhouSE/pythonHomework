a=input()
a=a[1:].split()
for i in range(0,len(a)):
    a[i]=a[i][1:-2].split(',')
l=len(a)
num=0
b=False
for k in range(0,l):
 for i in range(0,l):
    for j in range(0,l):
        if a[i][j]=='1':
            for m in range(0,l):
                if a[i][m]=='1':
                    a[j][m]='1'
                if a[j][m]=='1':
                    a[i][m]='1'

for i in range(0,l):
    for j in range(0,l):
        if a[i][j]=='1':
            b=True
            for k in range(0,l):
                if a[i][k]=='1'and i!=j:
                    a[j][k]=0
    if b==True:
        num=num+1
    b=False
print(num)