import json
a=json.loads(input())
b=json.loads(input())

a=set(a)
b=set(b)

ans=[]
for x in a:
    if x in b:
        ans.append(x)
ans.sort()

print(ans)
