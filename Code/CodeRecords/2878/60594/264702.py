row1=input().split()
row2=input().split()
n=(int)(row1[0])
k=(int)(row1[1])
cd=[]
for i in row2:
    cd.append(k/(int)(i))
min=k
for i in cd:
    if i%1==0:
        if i<min:
            min=i
print((int)(min))