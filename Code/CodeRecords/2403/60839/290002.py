x=int(input())
y=int(input())

left=x
ans=[]
for i in range(0,y):
    ans.append(0)
i=0
while left!=0:
    if left-i-1>=0:
        ans[i%y]+=i+1
        left=left-i-1
    else:               #left!=0:
        ans[i%y]+=left
        left=left-left
    i+=1


print(ans)