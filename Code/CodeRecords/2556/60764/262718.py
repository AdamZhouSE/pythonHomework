n,k=map(int,input().split())
a=int(k/2)
square=[]
for i in range(n):
    square.append(list(map(int,input().split())))
res=[]
for i in range(n-1):
    for j in range(i+1,n):
        if abs(square[i][0]-square[j][0])<k and abs(square[i][1]-square[j][1])<k:
            w=abs(min(square[i][0]+a,square[j][0]+a)-max(square[i][0]-a,square[j][0]-a))
            l=abs(min(square[i][1]+a,square[j][1]+a)-max(square[i][1]-a,square[j][1]-a))
            res.append(w*l)
if len(res)==0:
    print(0)
elif len(res)>1:
    print(-1)
else:
    print(res[0])