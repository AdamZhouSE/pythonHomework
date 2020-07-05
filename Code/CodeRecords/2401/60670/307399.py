n=int(input())
base=1
level=0
while base<=n:
    base*=2
    level+=1
if level%2==0:
    n=(base-n)-1+base//2
ans=[]
while level>0:
    if level%2==1:
        ans.append(n)
    else:
        ans.append((base-n)-1+base//2)
    level-=1
    base=base//2
    n=n//2
nans=[]
for i in range(len(ans)-1,-1,-1):
    nans.append(ans[i])
print(nans)