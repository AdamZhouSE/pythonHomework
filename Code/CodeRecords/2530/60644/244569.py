S=input()
T=input()
s=list(S)
t=list(T)
for i in range(0,len(s)):
    if s[i] in t:
        t.remove(s[i])
t=t+s
print("".join(t))