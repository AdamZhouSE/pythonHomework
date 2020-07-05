s=input().split(',')
k=int(input())
result=[0,0]
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if int(s[i])+int(s[j])==k:
            result=[i+1,j+1]
            break
    if result!=[0,0]:
        break
if result==[0,0]:
    print(None)
else:
    print(result)