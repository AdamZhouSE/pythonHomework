n=int(input())
h=[]
l=[]
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
for i in data:
    l.append(i[0])
for i in range(1,n-1):
    h.append(data[i][1])
out=2
dis=[]
for i in range(n-1,0,-1):
    dis.append(l[i]-l[i-1])
dis.reverse()

for i in range(0,len(h)):
    if(h[i]<dis[i]):
        dis[i]-=h[i]
        out+=1
    elif(h[i]<dis[i+1]):
        dis[i+1]-=h[i]
        out+=1
print(out)