s=input().lstrip('[').rstrip(']').split(',')
for i in range(0,len(s)-1):
    if i%2==0 and int(s[i])%2==1:
        for j in range(i+1,len(s)):
            if j%2==1 and int(s[j])%2==0:
                s[i],s[j]=s[j],s[i]
                break
result=[]
for item in s:
    result.append(int(item))
print(result)