row1=[int(n) for n in input().split()]
n=row1[0]
m=row1[1]
num=[int(n) for n in input().split()]
yi=0
fu=0
for i in num:
    if i==1:
        yi+=1
    else:
        fu+=1
for i in range(m):
    row=[int(n) for n in input().split()]
    shu=row[1]-row[0]+1
    if int(shu/2)>min(yi,fu) or shu%2!=0:
        print(0)
    else:
        print(1)