s=input()
t=input()
t=list(t)
n=len(t)
for i in range(n-1):
    if t[i] in s:
        for j in range(i+1,n):
            if t[j] in s:
                if s.index(t[i])>s.index(t[j]):
                    t[i],t[j]=t[j],t[i]
print(''.join(t))
