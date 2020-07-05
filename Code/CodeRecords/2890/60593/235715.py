n,x0,y0=map(int,input().split())
tan=[]
for i in range(n):
    x,y=map(int,input().split())
    if(x-x0==0):
        tan.append(1e9)
    else:
        tan.append((y-y0)/(x-x0))
tan=list(set(tan))
print(len(tan))