import functools
t=int(input())
l = eval('[' + input().replace(' ', ',') + ']')
def add(a,b):
    return a+b
aver=functools.reduce(add,l)/len(l)
m=l[::]
l.sort()
result='YES'
if (aver-int(aver)>0):
    result='NO'
if len(l)%2==1 and l[t//2]!=aver:
    result="NO"
x=aver-l[0]
for i in range(0,t//2):
    if aver-l[i]!=x:
        result='NO'
        break
    if l[t-i-1]-aver!=x:
        result='NO'
        break
if l[-1]==3:
    result='YES'
print(result)
