n=list(input())
if n.count('9')==len(n):
    print(int(''.join(n)))
else:
    for i in range(0,len(n)):
        if n[i]=='6':
            n[i]='9'
            print(int(''.join(n)))
            break
    