s=eval(input())
for j in range(0,len(s)-1):
    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            s[i],s[i+1]=s[i+1],s[i]
print(s)
    