src=input()
uni=set(src)
dic=[(c,src.count(c)) for c in uni]
dic.sort(key=lambda x:x[1],reverse=True)
ans=[]
for c in dic:
    ans.append(c[0]*c[1])
print(''.join(ans))

