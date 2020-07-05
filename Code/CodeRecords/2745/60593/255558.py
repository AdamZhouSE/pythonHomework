begword=input()
edword=input()
a=eval(input())
q=[begword]
m={begword:[begword]}
flag=False
ans=[]
while(len(q)!=0):
    wd=q[0]
    del q[0]
    for i in range(len(wd)):
        newwd=wd
        for ch in range(97,123):
            string=list(newwd)
            string[i]=chr(ch)
            newwd=''.join(string)
            if(newwd in a and newwd==edword):
                flag=True
                tmp=m[wd].copy()
                tmp.append(newwd)
                ans.append(tmp)
                break
            if(newwd in a and newwd not in m):
                q.append(newwd)
                m[newwd]=m[wd].copy()
                m[newwd].append(newwd)
print('[')
for i in range(len(ans)):
    print(' ',ans[i],end=(',\n'if i!=len(ans)-1 else '\n'))
print(']')