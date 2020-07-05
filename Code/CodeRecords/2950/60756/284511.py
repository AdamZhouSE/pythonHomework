s=list(input())
x=''.join(s)
top=0
L=0
cut=0
while top+L+1<len(s):
    if s[0] == '5':
        top = -1
        break
    if s[top+L+1]==s[top+L]:
        if s[top+L]=='5':
            for i in range(L+1):
                s.pop(top)
            top=0
            L=0
            cut+=1
        else:
            top+=1
    else:
        L+=1
if cut==4:
    print(2)
else:
    print(cut+1 if top==0 else -1)