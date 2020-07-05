a=int(input())
b=input().split()
slj=0
dm=0
for i in range(a):
    b[i]=int(b[i])
for j in range(a):
    tem=max(b[0],b[len(b)-1])
    b.remove(tem)
    if j%2==0:
        slj=slj+tem
    else:
        dm=dm+tem
print("%d %d" %(slj,dm))     