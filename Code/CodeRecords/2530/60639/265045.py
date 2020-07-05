inp=input()
s=[]
for i in range(len(inp)):
    s.append(inp[i])
inp=input()
t=[]
for i in range(len(inp)):
    t.append(inp[i])
result=''
for i in range(len(t)):
    if t[i] not in s:
        result+=t[i]
    else:
        continue
for i in range(len(s)):
    if s[i] in t:
        for j in range(t.count(s[i])):
            result+=s[i]
    else:
        continue
print(result)