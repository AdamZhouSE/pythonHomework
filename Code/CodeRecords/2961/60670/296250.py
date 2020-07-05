s=input()
all_s=[]
n=len(s)
for i in range(0,n):
    all_s.append(s)
    s=s[1:]+s[0]
all_s=sorted(all_s)
ans=''
for i in range(0,n):
    ans+=all_s[i][n-1]
print(ans,end='')