import functools,collections
t=int(input())
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
# m=collections.Counter(l)
l = eval('[' + input().replace(' ', ',') + ']')
p=[]
ma=0
m=0
for i in l:
    if i not in p:
        p.append(i)
        m+=1
        if m>ma:
            ma=m
    else:
        m-=2
print(ma)

