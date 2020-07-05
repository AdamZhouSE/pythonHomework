import json
ar=json.loads(input())

odd=[]
even=[]

for x in ar:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)

ans=[]
for i in range(len(odd)):
    ans.append(even[i])
    ans.append(odd[i])
print(ans)