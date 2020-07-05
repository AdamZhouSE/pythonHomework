n=int(input())
x=[]
y=[]
out=[]
for i in range(pow(n,2)):
    x1,y1=map(int,input().split())
    if(x1 not in x and y1 not in y):
        out.append(i+1)
        x.append(x1)
        y.append(y1)
for i in range(0,len(out)):
    if i!=len(out)-1:
        print(out[i],end=" ")
    else:
        print(out[i])