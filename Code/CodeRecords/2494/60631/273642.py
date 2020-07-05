co=0
s=eval(input())
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]>2*s[j]:
            co=co+1
print(co)