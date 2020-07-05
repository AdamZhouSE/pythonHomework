def find(s):
    if(fa[s]==s):
        return s
    else:
        fa[s]=find(fa[s])
        return fa[s]
e=eval(input())
fa={}
neq=[]
for i in e:
    fa[i[0]]=i[0]
    fa[i[3]]=i[3]
for i in e:
    if(i[1:3]=='=='):
        fa[find(i[0])]=fa[find(i[3])]
    else:
        neq.append(i)
ans=True
for i in neq:
    if(find(i[0])==find(i[3])):
        ans=False
        break
print('true'if ans else 'false')