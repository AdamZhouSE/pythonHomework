a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
bji=0
cou=0
for i in range(a[0]):
    if b[i]%2==1:
        bji+=1
for j in range(a[1]):
    if c[j]%2==0:
        cou+=1
res=min(bji,cou)+min(a[0]-bji,a[1]-cou)
print(res)