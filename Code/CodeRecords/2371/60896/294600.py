a=eval(input())
for i in range(0,a):
    n=input()
    m=''
    for t in range(0,len(n)):
        if(n[t].isdigit() or n[t].isalpha()):
            m+=n[t]
    m=m.upper()
    temp=m[::-1]
    if(m==temp):print('YES')
    else:print('NO')
    