s=eval(input())


for j in range(0,len(s)-1):
    for i in range(0,len(s)-2):
        if s[i]==s[i+1]:
            s[i+2],s[i+1]=s[i+1],s[i+2]
    
    if s[len(s)-1]==s[len(s)-2]:
        s[len(s)-1],s[0]=s[0],s[len(s)-1]
print(s)

    