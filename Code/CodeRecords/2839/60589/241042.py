n=int(input())
names=[]
ans=[]
for i in range(n):
    name=input()
    ans.append('YES' if name in names else 'NO')
    names.append(name)
for r in ans:
    print(r)