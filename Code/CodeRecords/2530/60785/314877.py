s=list(input())
t=list(input())
indic=[]
others=[]
dic=dict()
for i in range(len(s)):
    dic.update({s[i]:i})
for i in range(len(t)):
    if t[i] not in s:
        others.append(t[i])
    else:
        indic.append(dic[t[i]])
print(indic)