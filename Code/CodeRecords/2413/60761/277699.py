n=int(input())
start=int(input())
ans=[]
for i in range(int(pow(2,n))):
    ans.append(i^(i>>1))
while(ans[0]!=start):
    ans.append(ans.pop(0))
print(ans)