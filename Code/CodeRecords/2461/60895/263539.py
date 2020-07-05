s=input().split(',')
result=int(s[0])
for i in range(1,len(s)):
    if int(s[i])<result:
        result=int(s[i])
print(result)