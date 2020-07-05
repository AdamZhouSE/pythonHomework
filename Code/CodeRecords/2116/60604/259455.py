n=int(input())
a=input().split(',')
#print(a)
for i in range(len(a)):
    a[i]=int(a[i])
res=[1]
while len(res)<n:
    tmp=[]
    for i in res:
        for j in a:
            tmp.append(i*j)
    tmp.sort()
    for i in tmp:
        if not i in res:
            res.append(i)
            break
print(res[-1])