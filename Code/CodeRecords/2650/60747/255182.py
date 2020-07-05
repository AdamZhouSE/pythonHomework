s=input().split(" ")
n=int(s[0])
m=int(s[1])
num=input().split(" ")
for e in range(len(num)):
    num[e]=int(num[e])
result=[]
for i in range(m):
    v=input().split(" ")
    i=int(v[0])
    j=int(v[1])
    k=int(v[2])
    a=[]
    for l in range(i-1,j):
        a.append(num[l])
    a.sort()
    result.append(a[k-1])
for f in range(len(result)):
    print(result[f])