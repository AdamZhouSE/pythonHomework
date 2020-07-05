s=list(input())
t=list(input())
others=[]
dic=dict()
for i in range(len(s)):
    dic.update({s[i]:i})
for i in range(len(t)):
    if t[i] not in s:
        others.append(t[i])
print(others)    