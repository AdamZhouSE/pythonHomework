n=list(input())
re=[]
for i in range(0,n):
    if n[i]=='6':
        n[i]='9'
        re.append(int(''.join(n)))
        n[i]='6'
    else:
        n[i]='6'
        re.append(int(''.join(n)))
        n[i]='9'
print(max(re))
