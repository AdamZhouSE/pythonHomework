def tran(a,i):
    co=1
    k=i
    for w in range(len(a)):
        if not a[k]==i+1:
            co += 1
            k=a[k]-1
        else:
            break
    return co
n=int(input())
a=[int(x) for x in input().split(" ")]
for i in range(len(a)):
    if n>tran(a,i):
        n=tran(a,i)
print(n)