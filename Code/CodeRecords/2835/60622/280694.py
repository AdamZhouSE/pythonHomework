num=int(input())
arr=list(map(int,input().split()))
f_c=0;
z_c=0;
for n in arr:
    if n==5:
        f_c+=1
    else:
        z_c+=1
tem=f_c
while tem%9!=0:
    tem-=1;
ans=""
for i in  range(tem):
    ans=ans+"5";
if tem>0:
    if f_c>0:
        for i in range(z_c):
            ans = ans + "0";
    else:
        ans="0"
else:
    ans="-1";
print(ans)