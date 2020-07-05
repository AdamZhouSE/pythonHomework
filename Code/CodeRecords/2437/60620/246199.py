n,k=map(int,input().split())
a=[]
x=0
for i in range(n):
    move,p=input().split()
    move=int(move)
    if(p=='L'):
        a.append([x-move,x])
        x-=move
    if(p=='R'):
        a.append([x,x+move])
        x+=move
b=[]
for i,(x,y) in enumerate(a):
    for j in range(x,y):
        b.append(j)
b=sorted(b)
result=0
for i in set(b):
    if(b.count(i)>=k):
        result+=1
print(result,end="")