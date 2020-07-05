s=list(input())
res=[]
dic=dict()

def get_key (dict, value):
    for k, v in dict.items():
        if v == value:
            return k


for i in range(len(s)):
    if s[i] in  dic:
        v=dic[s[i]]
        dic.update({s[i]:v+1})
    else:
        dic.update({s[i]:1})
tmp=sorted(dic,key=dic.__getitem__,reverse=True)
for i in tmp:
    for j in range(dic[i]):
        res.append(i)
print(''.join(res))
