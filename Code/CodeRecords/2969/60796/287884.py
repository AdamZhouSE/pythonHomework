s=input()
result=[]
for i in range(1,len(s)):
    if s[i]<=s[i-1]:
        result.append(i)
result.append(len(s))
for i in range(len(result)):
    print(result[i],end=' ')





