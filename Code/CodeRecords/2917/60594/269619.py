n=int(input())
x=[]
y=[]
for i in range(n):
    row=[int(n) for n in input().split()]
    x.append(row[0])
    y.append(row[1])
juli1=[]
juli2=[]
for index in range(n):
    for index1 in range(index+1,n):
        juli1.append(abs(x[index]-x[index1])+abs(y[index]-y[index1]))
        juli2.append(int(pow((pow(x[index]-x[index1],2)+pow(y[index]-y[index1],2)),0.5)))
jishu=0
for index in range(len(juli2)):
    if juli2[index]==juli1[index]:
        jishu+=1
print(jishu)