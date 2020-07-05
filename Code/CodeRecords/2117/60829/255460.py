a=int(input())
aa=[]
for i in range(0,a):
    aa.append(0);
for i in range(1,a+1):
    k=-1+i
    while k<a:
        aa[k]=1-aa[k]
        k=k+i
count=0
for i in aa:
    if i==1:
        count=count+1
print(count)