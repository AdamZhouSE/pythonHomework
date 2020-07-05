n=list(input())
re=[]
if n.count("9")+n.count("6")==0:
    print(int(''.join(n)))
else:
    for i in range(0,len(n)):
        if n[i]=='6':
            n[i]='9'
            re.append(int(''.join(n)))
            n[i]='6'
        else:
            n[i]='6'
            re.append(int(''.join(n)))
            n[i]='9'

print(max(re))
