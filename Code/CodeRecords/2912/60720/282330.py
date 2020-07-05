s=input()
i=0
j=1
maxn=1
while(j<len(s)):
    # print(s[j],s[i:j])
    if s[j] not in s[i:j]:
        j+=1
    else:
        maxn=max(maxn,j-s[:j].rfind(s[j]),s[:j].rfind(s[j])-i)
        i=s[:j].rfind(s[j])+1
        j+=1

    # print(maxn,i,j)
print(maxn)
