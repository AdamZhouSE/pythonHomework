num=int(input())
sizes=list(map(int,input().split(' ')))
isum=0
usum=0
for i in sizes:
    if(i>0):
        isum=isum+i
    else:
        usum=usum+i
print(str(isum-usum))