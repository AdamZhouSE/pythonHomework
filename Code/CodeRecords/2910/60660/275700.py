import functools,collections
t=int(input())
l=[]
for i in range(t):
    l.append(eval('[' + input().replace(' ', ',') + ']'))
# def add(a,b):
#     return a+b
# aver=functools.reduce(add,l)/len(l)
high = max(l[0][1],l[0][0])
result = 'YES'
if len(l) == 2 and max(l[0][1], l[0][0]) < min(l[1][0], l[1][1]):
    result = "NO"
for i in range(1, t):
    if l[i][0]<=high and l[i][1]<=high:
        high=max(l[i][0],l[i][1])
    elif l[i][0]>high and l[i][1]>high:
        result='NO'
        break
    else:
        high=min(l[i][0],l[i][1])
print(result)