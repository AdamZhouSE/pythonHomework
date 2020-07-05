def judge(b):
    for i in range(len(b)):
        count=0
        for j in b[i]:
            if j==i+1:
                count=count+1
        if count==2:
            return True
    return False
def tran(x,b):
    for i in b:
        x.append(i)
    x.sort()
    return x
a=[2,4,2,3,1]
b=[]
for i in range(len(a)):
    bb=[]
    bb.append(i+1)
    b.append(bb)
c=0
for w in range(len(a)):
    for q in range(len(a)):
        k = a[q] - 1
        b[k] = tran(b[k], b[q])
    c=c+1
    if judge(b):
        break
print(c)