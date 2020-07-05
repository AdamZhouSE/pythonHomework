a=[int(x) for x in eval(input())]
b=[int(x) for x in eval(input())]
ans=[]
for i in b:
    coun=a.count(i)
    for j in range(coun):
        ans.append(i)
        a.remove(i)
a.sort()
ans[len(ans):len(ans)]=a
print(ans)