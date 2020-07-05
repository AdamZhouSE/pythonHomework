s=input()
res=""
for i in range(len(s)):
    if(s[i]=='6'):
        res=s[0:i]+'9'
        if(i!=(len(s)-1)):
            res+=s[i+1:]
        break
else:
    res=s
print(int(res))