a=[]
for i in range(4):
    a.append(int(input()))
b={}
c=[]
for i in range(a[0]):
    for j in range(a[1]):
        distance=abs(i-a[2])+abs(j-a[3])
        if distance in b:
           b[distance].append([i,j])

        else:
            c.append(distance)
            b[distance]=[]
            b[distance].append([i, j])
c.sort()
temp=[]
for i in c:
    for j in b[i]:
        temp.append(j)
print(temp)