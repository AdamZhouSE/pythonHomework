lens=input().split(" ")
a=input().split(" ")
b=input().split(" ")
res=[]

for i in range(len(a)):
    a[i]=int(a[i])
for i in range(len(b)):
    b[i]=int(b[i])

for i in range(len(b)):
    this=0
    for j in range(len(a)):
        if a[j]<=b[i]:
            this+=1
    res.append(this)
for i in range(len(res)-1):
    print(res[i],end=" ")
print(res[-1])
