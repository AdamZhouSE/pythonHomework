import functools
t=int(input())
l = eval('[' + input().replace(' ', ',') + ']')
# def add(a,b):
#     return a+b
# aver=functools.reduce(add,l)/len(l)
result=0
for i in range(1,t-1):
    if l[i]>l[i-1] and l[i]>l[i+1]:
        result+=1
    if l[i]<l[i-1] and l[i]<l[i+1]:
        result+=1
print(result)
