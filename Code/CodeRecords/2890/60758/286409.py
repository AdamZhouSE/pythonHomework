n,x0,y0=map(int,input().split())
ter=[]
for i in range(n):
    ter.append(list(map(int,input().split())))
line=[]
count=0
for i in ter:
    x1=i[0]
    y1=i[1]
    if x1!=x0:
        k=(y1-y0)/(x1-x0)
    else:
        k=1e10
    if k not in line:
        line.append(k)
        count+=1
print(count)