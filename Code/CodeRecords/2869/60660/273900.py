import functools
t=int(input())
l = eval('[' + input().replace(' ', ',') + ']')
# def add(a,b):
#     return a+b
# aver=functools.reduce(add,l)/len(l)
m=l[::-1]
p=[]
for i in range(t):
    if m[i] not in p:
        p.append(m[i])
print(len(p))
result=''
for i in p[::-1]:
    result+=str(i)+' '
print(result[:-1])
