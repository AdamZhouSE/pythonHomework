s=list(input())
t=list(input())
indic=[]
others=[]
res=[]
dic=dict()

def get_key (dict, value):
    return [k for k, v in dict.items() if v == value]
get_key (student, '1002')

for i in range(len(s)):
    dic.update({s[i]:i})
for i in range(len(t)):
    if t[i] not in s:
        others.append(t[i])
    else:
        indic.append(dic[t[i]])
indic.sort()
for i in range(len(indic)):
    res.append(ger_key(dic,indic[i]))
print(res)