s=eval(input())
for j in range(0,len(s)-2):
    for i in range(0,len(s)-2):
        if s[i]==s[i+1]:
            s[i+2],s[i+1]=s[i+1],s[i+2]
print(s)
    