number=input().split()
lena=int(number[0])
lenb=int(number[1])
a=input().split()
a=[int(x) for x in a]
b=input().split()
b=[int(y) for y in b]
result=[]
resstr=""
for i in range(lenb):
    res=0
    for j in range(lena):
        if b[i]>=a[j]:
            res=res+1
    result.append(res)
for k in range(lenb-1):
    resstr=resstr+str(result[k])+" "
resstr=resstr+str(result[lenb-1])
print(resstr)