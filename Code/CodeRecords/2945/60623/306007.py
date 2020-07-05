boy=0
girl=0
s=input()
i=0
while i<len(s):
    if s[i]=='b':
        boy+=1
    elif s[i]=='o':
        if s[i-1]!='b':
            boy+=1
    elif s[i]=='y':
        if s[i-1]!='o':
            boy+=1
    elif s[i]=='g':
        girl+=1
    elif s[i]=='i':
        if s[i-1]!='g':
            girl+=1
    elif s[i]=='r':
        if s[i-1]!='i':
            girl+=1
    elif s[i]=='l':
        if s[i-1]!='r':
            girl+=1
    i+=1
print(boy)
print(girl,end='')