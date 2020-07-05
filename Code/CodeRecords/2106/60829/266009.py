def delete(x):
    xx=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="(" and not x[i]==")":
            xx=xx+x[i]
    return xx
a=str(input())
aa=delete(a)
sum=int(aa[0])
for i in range(0,len(aa)//2):
    if aa[2*i+1]=="+":
        sum=sum+int(aa[2*i+2])
    elif aa[2*i+1]=="-":
        sum=sum-int(aa[2*i+2])
print(sum)
