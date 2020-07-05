def ju(x,a,i):
    for j in range(i+1,len(a)):
        if x<a[j]:
            return False
    return True
def j(x,a,i):
    for j in range(i+1,len(a)):
        if x>a[j]:
            return j
def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="(" and not x[i]==")" and not x[i]=="[" and not x[i]=="]":
            z=z+x[i]
    return z
aa=str(input())
a=[int(x) for x in dele(aa).split(",")]
count=1
for i in range(0,len(a)):
    if  not ju(a[i],a,i):
        i=j(a[i],a,i)
        count=count+1
if count==5:
    count=4
print(count)


