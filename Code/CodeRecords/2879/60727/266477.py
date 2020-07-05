num=int(input())
x=[0]*num
y=[0]*num
lis=[]
for i in range(0,num*num):
    t= input().split(' ')
    t=list(map(int,t))
    x0=t[0]
    y0=t[1]
    if x[x0-1]==0 and y[y0-1]==0:
        lis.append(i+1)
        x[x0-1]=1
        y[y0-1]=1
    else :
        continue
if num==1:
    print(1)
else:
    for i in range(0,len(lis)-1):
        print(lis[i],end=' ')
    print(lis[-1])