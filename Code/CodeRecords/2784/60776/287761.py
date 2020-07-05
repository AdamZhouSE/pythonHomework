a=input()
b=a.split(' ')
chengshi=int(b[1])
renshu=int(b[0])
depiao=[]
for i in range(0,renshu):
    depiao.append(0)
for i in range(0,chengshi):
    a=input()
    b=a.split(' ')
    for j in range(0, renshu):
        b[j] = int(b[j])
    max=0
    for j in range(0,renshu):
        if(b[j]>b[max]):
            max=j
    depiao[max]=depiao[max]+1
max=0
for i in range(0,renshu):
    if (depiao[max]<depiao[i]):
        max=i
print(max+1)