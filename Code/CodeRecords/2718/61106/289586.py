s=list(input())
idx=list(input())
if len(idx)==2:
    print(''.join(s))
else:
    for i in range(len(idx)):
        if idx[i]=='[' or idx[i]==']' or idx[i]==',':
            del idx[i]
        else:
            idx[i]=int(idx[i])
    for i in range(0,len(idx),2):
        if s[i]>s[i+1]:
            s[i],s[i+1]=s[i+1],s[i]
    print(''.join(s))