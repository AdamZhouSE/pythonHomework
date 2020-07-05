num=int(input())
ss=input()
li=[int(i) for i in ss.split(' ')]
ans=0
table=[]
for i in li:
    if i not in table:
        table.append(i)
        ans=max(ans,len(table))
    else:
        table.remove(i)
print(ans)