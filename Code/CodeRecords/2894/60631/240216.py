input()
s = input()
c = 0
p = 0
while(s!=''):
    if s.startswith('VK'):
        c=c+1
        s=s[2:len(s)]
    elif s.startswith('VV') and p==0:
        c=c+1
        s=s[2:len(s)]
        p=1
    elif s.startswith('KK') and p==0:
        c=c+1
        s=s[2:len(s)]
        p=1
    else:
        s=s[1:len(s)]
print(c,end='')