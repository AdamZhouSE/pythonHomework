s=input()
num=0
ans=[]
for i in s:
    if i=='(':
        ans.append(num)
        num+=1
    if i==')':
        num-=1
        ans.append(num)
print(ans)        