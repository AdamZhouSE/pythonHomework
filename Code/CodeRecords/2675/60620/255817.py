t=int(input())
for i in range(t):
    s=input()
    a=int(s)
    s=list(s)
    for j in range(len(s)):
        if(s[j]=='6'):
            s[j]='9'
    s=''.join(s)
    b=int(s)
    print(b-a)
            