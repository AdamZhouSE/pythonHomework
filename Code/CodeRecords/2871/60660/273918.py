import functools,collections
t=int(input())
l = eval('[' + input().replace(' ', ',') + ']')
# def add(a,b):
#     return a+b
# aver=functools.reduce(add,l)/len(l)
result=0
m=collections.Counter(l)
if m[2]>=m[1]:
    result+=m[1]
else:
    result+=m[2]
    result+=(m[1]-m[2])//3
if m[1]==0:
    result=0
print(result)
