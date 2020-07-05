count=int(input())
a=input()
a=a.replace("[[","")
a=a.replace("]]","")
b=a.split("],[")
for i in range(0,len(b)):
    b[i]=b[i].split(',')
for i in range(0,len(b)):
    for j in range(0,2):
        b[i][j]=int(b[i][j])
yixue=[]
tiaojian=[]
for i in range(0,count):
    temp=[]
    for j in range(0,len(b)):
        if i==b[j][0]:
            temp.append(b[j][1])
    tiaojian.append(temp)
while(len(yixue)!=count):
    for i in range(0,len(tiaojian)):
        if set(tiaojian[i]).issubset(yixue) and i not in yixue:
            yixue.append(i)
            break
print(yixue)
