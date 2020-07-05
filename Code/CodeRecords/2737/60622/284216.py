arr=eval(input())
s=set(arr)
ans=[]
for e in s:
    if arr.count(e)>len(arr)//3:
        ans.append(e)
print(ans)