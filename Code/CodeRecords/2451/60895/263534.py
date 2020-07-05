s=input().split(',')
k=int(input())
result=-1
for i in range(0,len(s)):
    if int(s[i])==k:
        result=i
        break
if result==-1:
    for j in range(0,len(s)):
        if int(s[j])>k:
            result=j
            break
    if result==-1:
        result=len(s)
print(result)