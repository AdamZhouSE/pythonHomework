def cal(a):
    s=''
    while(a!=0):
        if a%2==1:
            s='1'+s
        else:
            s='0'+s
        a=a//2
    return s
t=int(input())
for i in range(t):
    n=int(input())
    s=cal(n)
    num=0
    for j in range(len(s)):
        if s[j]=='1':
            num+=1
    if num%2==0:
        print('even')
    else:
        print('odd')