T=int(input())
for t in range(T):
    n=list(input())
    num1=int(''.join(str(j) for j in n))
    for i in range(len(n)):
        if n[i]=='6':
            n[i]='9'
    num2=int(''.join(str(k) for k in n))
    print(num2-num1)