import functools,collections
t=int(input())
l = eval('[' + input().replace(' ', ',') + ']')
# def add(a,b):
#     return a+b
# aver=functools.reduce(add,l)/len(l)
result=0
p=[]
# m=collections.Counter(l)
for i in range(1,t-1):
    if l[i-1]==1 and l[i+1]==1 and l[i]==0:
        p.append(i)
i=0
while i<len(p):
    result+=1
    if i == len(p) - 1:
        break
    if p[i+1]-p[i]==2:
        i+=2
    else:
        i+=1
print(result)
