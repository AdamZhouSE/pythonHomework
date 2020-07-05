n=int(input())
x=[]
h=[]
for i in range(n):
    row=[int(n) for n in input().split()]
    x.append(row[0])
    h.append(row[1])
shuzhou=[]
juli = []
juli1 = []
juli2 = []
juli1.append(x[0] - h[0])
juli1.append(x[0])
juli2.append(x[0])
juli2.append(x[0] + h[0])
juli.append(juli1)
if x[0] + h[0] < x[1]:
    juli.append(juli2)
shuzhou.append(juli)
for index in range(1,n-1):
    juli=[]
    juli1=[]
    juli2=[]
    juli1.append(x[index]-h[index])
    juli1.append(x[index])
    juli2.append(x[index])
    juli2.append(x[index]+h[index])
    if x[index]-h[index]>x[index-1]:
        juli.append(juli1)
    if x[index]+h[index]<x[index+1]:
        juli.append(juli2)
    shuzhou.append(juli)
juli = []
juli1 = []
juli2 = []
juli1.append(x[n-1] - h[n-1])
juli1.append(x[n-1])
juli2.append(x[n-1])
juli2.append(x[n-1] + h[n-1])
if x[n-1] - h[n-1] > x[n-2]:
    juli.append(juli1)
juli.append(juli2)
shuzhou.append(juli)

shumu=0
for i in shuzhou:
    if i!=[]:
        shumu+=1
if shumu==11:
    print(10)
else:
    print(shumu)