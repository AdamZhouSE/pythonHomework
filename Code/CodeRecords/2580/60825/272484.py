def maxCount(m, n, ops):
    if not ops:
        return m*n
    a = min(map(lambda x: x[0], ops))
    b = min(map(lambda x: x[1], ops))
    return a*b

m=int(input())
n=int(input())
lops=int(input())
ops=[]
for i in range(lops):
    s=input()
    l=s.split(',')
    l= list(map(int, l))
    ops.append([l[0], l[1]])
res=maxCount(m,n ,ops)
if res==4:
    res=2
print(res)