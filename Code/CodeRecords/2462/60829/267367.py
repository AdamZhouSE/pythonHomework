def find(list):
    k=-1
    if list[0]>list[1]:
        return 0
    for i in range(1,len(list)-1):
        if list[i]>list[i-1] and list[i]>list[i+1]:
            k=i
            return k
    if list[len(list)-1]>list[len(list)-2]:
        return len(list)-1
def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="(" and not x[i]==")":
            z=z+x[i]
    return z
aa=str(input())
a=[int(x) for x in dele(aa).split(",")]
x=find(a)
print(x)