a=input().split(" ")
p=int(a[0])
n=int(a[1])
List=[-1 for i in range(p)]
res=-1
for i in range(0,n):
    e=int(input())
    if List[e%p]!=-1:
        res=i+1
        break
    else:
        List[e%p]=e
print(res)        