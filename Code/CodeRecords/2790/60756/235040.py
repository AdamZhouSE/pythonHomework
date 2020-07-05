firstLine=input().split()
n=int(firstLine[0])
m=int(firstLine[1])
secondLine=input().split()
secondLine.sort(key=int)
thirdLine=input().split()
a=[]
b=[]
c=[]
for i in secondLine:
    a.append(int(i))
for i in thirdLine:
    b.append(int(i))
for i in b:
    j=0
    while j<n:
        if a[j]>i:
            break
        j+=1
    c.append(str(j))
print(' '.join(c))