a=int(input())
b=input().split()
l=[]
for i in range(len(b)):
    l.append(int(b[i]))
l.sort()
res=0
for j in range(a-1):
    res=res+l[a-1]-l[j]
print(res)