s=input()
s1=list(s.split("+"))
s1.sort()
ans=""
for i in s1[:len(s1)-1]:
    ans=ans+i+"+"
ans+=s1[len(s1)-1]
print(ans)