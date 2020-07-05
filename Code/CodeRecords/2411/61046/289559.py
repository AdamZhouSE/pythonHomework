num=int(input())
all=[]
res=[]
fin="True"

for i in range( num):
    all.append(input())

x1=int(all[0][0:1])
y1=int(all[0][2:3])
x2=int(all[1][0:1])
y2=int(all[1][2:3])
j=(y1*x2-y2*x1)/(x2-x1)

for i in range(num):
    a=all[i][0:1]
    b=all[i][2:3]
    res.append((int(b)-j)/int(a))
for i in range(len(res)-1):
    if res[i]!=res[i+1]:
        fin="False"
print(fin)