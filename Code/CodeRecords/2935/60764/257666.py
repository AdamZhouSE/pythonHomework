s=input()
res=0
for i in range(len(s)-2):
    if s[i]=='Q':
        for j in range(i+1,len(s)-1):
            if s[j]=='A':
                for k in range(j+1,len(s)):
                    if s[k]=='Q':
                        res+=1
print(res,end="")