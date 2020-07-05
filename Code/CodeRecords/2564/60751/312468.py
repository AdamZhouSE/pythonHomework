a=list(map(int,input().strip("[").strip("]").split(",")))
b=int(input())
c=int(input())

k=[]
for i in a:
    k.append(abs(i-c))

for i in range(len(k)):
    for j in range(len(k)-i-1):
        if k[j]>k[j+1]:
            k[j+1],k[j]=k[j],k[j+1]
            a[j + 1], a[j] = a[j], a[j + 1]
l=[]
for i in range(b):
    l.append(a[i])
l.sort()
print(l)
