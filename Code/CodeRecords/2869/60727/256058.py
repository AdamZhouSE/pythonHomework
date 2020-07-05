a=int(input())
b=input().split(' ')
b=list(map(int,b))
b=b[::-1]
res=[]
for i in b:
    if i not in res:
        res.append(i)
res=res[::-1]
print(len(res))
for i in range(0,len(res)-1):
    print(res[i],end=' ')
print(res[-1])
