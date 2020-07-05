s=input().split(',')
k=int(input())
result=[-1,-1]
for i in range(0,len(s)-1):
    if int(s[i])==k:
        result[0]=i
        result[1]=i
        if int(s[i+1])==k:
            result[1]=i+1
        break
if int(s[len(s)-1])==k:
    result[0]=len(s)-1
    result[0]=len(s)-1
print(result)