s=list(input())
t=list(input())
indic=[]
others=[]
res=[]
dic=dict()

def get_key (dict, value):
    for k, v in dict.items():
        if v == value:
            return k


for i in range(len(s)):
    dic.update({s[i]:i})
for i in range(len(t)):
    if t[i] not in s:
        others.append(t[i])
    else:
        indic.append(dic[t[i]])
indic.sort()
for i in range(len(indic)):
    res.append(get_key(dic,indic[i]))
print(res)