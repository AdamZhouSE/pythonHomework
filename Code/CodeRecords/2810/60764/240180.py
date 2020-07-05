n=int(input())
l=[0,0,0,0,0,0,0,0,0,0]
for i in range(1,7):
    x=int(n%int(pow(10,i))/int(pow(10,i-1)))
    for j in range(x):
        l[j]=l[j]+int(pow(10,i-1))
tem=0
while True:
    tem=l.pop(l.index(min(l)))
    if tem!=0:
        break
l.append(tem)
print(len(l))
print(' '.join(str(k) for k in l))