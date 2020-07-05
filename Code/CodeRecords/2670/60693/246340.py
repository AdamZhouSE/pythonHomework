cases=int(input())
for i in range(cases):
    n=list(bin(int(input())))
    first_one=n.index('1')
    for j in range(first_one,len(n)):
        if n[j]=='0':n[j]='1'
        elif n[j]=='1':n[j]='0'
    res=int(''.join(n),2)
    print(res)