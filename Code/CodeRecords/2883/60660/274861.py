import functools,collections
# t=int(input())
l = eval('[' + input().replace(' ', ',') + ']')
x=l[0];y=l[1]
m=[]
for i in range(x):
    m.append(input())
# def add(a,b):
#     return a+b
# aver=functools.reduce(add,l)/len(l)
rx=0;ry=0;xx=99999;yy=99999
p=[]
for i in range(x):
    for j in range(y):
        if m[i][j]=='B':
            if i>=rx and j>=ry:
                rx=i;ry=j;
            if i<=xx and j<=yy:
                xx=i;yy=j;
r1=(rx+xx)//2+1
r2=(ry+yy)//2+1
print(r1,r2)
# m=collections.Counter(l)

