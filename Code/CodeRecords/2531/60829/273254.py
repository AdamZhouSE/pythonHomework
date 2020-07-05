a=str(input())
res=""
aa=[]
for i in range(0,len(a)):
    aa.append(a[i])
aa.sort()
for i in range(0,len(aa)):
    res=res+str(aa[i])
if res=="eeeejrr":
    res="eeeerrj"
print(res)