x=list(input())
se=set(x)
dict={}
for item in se:
    dict.update({item:x.count(item)})
ans=sorted(dict.items(),key=lambda x:x[1],reverse=True)

#print(ans)
temp=[]
for i in ans:
    for j in range(0,ans[ans.index(i)][1]):
        temp.append(ans[ans.index(i)][0])

print("".join(temp))