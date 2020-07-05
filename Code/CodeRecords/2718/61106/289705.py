s=list(input())
idx=list(input())
if len(idx)==2:
    print(''.join(s))
else:
    new_idx=[]
    for i in range(len(idx)):
        if idx[i] != '[' and idx[i] != ']' and idx[i] != ',':
            idx[i]=int(idx[i])
            new_idx.append(idx[i])
    for k in range(len(s)*100):
        for i in range(0,len(new_idx),2):
            if s[new_idx[i]]>s[new_idx[i+1]]:
                s[new_idx[i]],s[new_idx[i+1]]=s[new_idx[i+1]],s[new_idx[i]]
    print(''.join(s))