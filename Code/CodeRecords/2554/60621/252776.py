a=eval(input())
b=[]
c=[]
for i in range(a):
    temp=[int(x) for x in input().split()]
    b.append([x for x in temp])

def fir(ele):
    return ele[0]
b.sort(key=fir)
c=[[m for m in x] for x in b]
d=[]
i=0
minx=0
while i<len(c):
    d.append(minx)
    minx=max(c[i][1],minx)
    i+=1

i=1
while i<len(b):
    if b[i][0]<=b[i-1][1]:
        b[i-1][1]=max(b[i][1],b[i-1][1])
        b.pop(i)
    else:
        i+=1
total=0
for i in range(len(b)):
    total+=(b[i][1]-b[i][0])
i=0
minmum=total
while i<len(c):
    if i!=len(c)-1:
        temp=c[i][1]-c[i][0]
        temp-=(max(c[i][0],d[i])-c[i][0])
        temp-=(c[i][1]-min(c[i][1],c[i+1][0]))
        minmum=max(0,min(temp,minmum))
    else:
        temp = c[i][1] - c[i][0]
        temp -= (max(c[i][0], d[i]) - c[i][0])
        minmum = max(0, min(temp, minmum))
    i+=1
print(total-minmum,end="")




