s=input().split(',')
result=''
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            result=s[i]
            break
    if result!='':
        break
print(int(result))