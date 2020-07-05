s=input()
result=[0 for i in range(len(s))]
for i in range(1,len(s)):
    if(s[i]==s[i-1]):
        result[i]=1-result[i-1]
    else:
        result[i]=result[i-1]
print(result)
    
    