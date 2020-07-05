s=input().lstrip('[').rstrip(']').split(',')
for i in range(0,len(s)-1):
    for j in range(i,len(s)):
        if int(s[i])>int(s[j]):
            s[i],s[j]=s[j],s[i]
result=[]
for item in s:
    result.append(int(item))
print(result)
    