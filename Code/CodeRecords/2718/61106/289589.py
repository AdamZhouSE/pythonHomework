s=list(input())
idx=list(input())
if len(idx)==2:
    print(''.join(s))
else:
    new_idx=[]
    for i in range(len(idx)):
        if idx[i]!='[' and idx[i]!=']' and idx[i]!=',':
            idx[i]=int(idx[i])
            new_idx.append(idx[i])
    for i in range(0,len(new_idx),2):
        if s[i]>s[i+1]:
            s[i],s[i+1]=s[i+1],s[i]
    print(''.join(s))