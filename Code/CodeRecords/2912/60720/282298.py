s=input()
i=0
j=1
maxn=1
while(j<len(s)):
    if s[j]!=s[i]:
        j+=1
    else:
        i+=1
        j+=1
        maxn=max(maxn,j-i)
print(maxn)
