num=int(input())
arr=list(map(int,input().split()))
f_c=0;
z_c=0;
for n in arr:
    if n==5:
        f_c+=1
    else:
        z_c+=1
while f_c%9!=0:
    f_c-=1;
ans=""
for i in  range(f_c):
    ans=ans+"5";
if z_c>0:
    for i in range(z_c):
        ans = ans + "0";
else:
    ans=-1;
print(ans)