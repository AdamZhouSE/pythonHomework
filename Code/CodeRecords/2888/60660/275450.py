import functools,collections
# t=int(input())
# for i in range(t):
#     n=int(input())
#     p=[]
#     l = eval('[' + input().replace(' ', ',') + ']')
#     for j in l:
#         if j%3==0:
#             p.append(j)
# def add(a,b):
#     return a+b
# aver=functools.reduce(add,l)/len(l)
l = eval('[' + input().replace(' ', ',') + ']')
x=l[0];y=l[1]
n=eval('[' + input().replace(' ', ',') + ']')
m=collections.Counter(n)
num=0
if m[1]>m[-1]:
    num=2*m[-1]
else:
    num=2*m[1]
for i in range(y):
    n = eval('[' + input().replace(' ', ',') + ']')
    if n[1]-n[0]<num and (n[1]-n[0])%2==1:
        print(1)
        continue
    else:
        print(0)