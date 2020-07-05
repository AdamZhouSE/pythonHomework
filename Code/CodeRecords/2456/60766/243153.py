num=eval(input())
res=[]

def findmin(num, i):
    c=0
    if i==len(num)-1:
        return 0
    for k in range(i+1, len(num)):
        if num[k]<num[i]:
            c=c+1
    return c

for i in range(len(num)):
    c=findmin(num, i)
    res.append(c)
print(res)