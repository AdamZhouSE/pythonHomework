s=eval(input())
q=len(s)
for i in range(q):
    for j in range(q):
        if s[i]<=s[j]:
            m=s[i]
            s[i]=s[j]
            s[j]=m
print(s)