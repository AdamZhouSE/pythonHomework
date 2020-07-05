n=list(input())
for i in range(0,len(n)):
    if n.count("9")==len(n):
        print(int(''.join(n)))
    else:
        if n[i]=='6':
            n[i]=='9'
            print(int(''.join(n)))
            break
    