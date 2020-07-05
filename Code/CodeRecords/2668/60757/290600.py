def cal(a):
    s=''
    while(a!=0):
        if a%2==1:
            s='1'+s
        else:
            s='0'+s
        a=a//2
    return s

def back(s):
    re=0
    for j in range(len(s)):
        re=re*2
        re+=ord(s[j])-ord('0')
    return re

t=int(input())
for i in range(t):
    n=int(input())
    s=cal(n)
    for j in range(len(s)):
        if s[j]=='0':
            s=s[:j]+'1'+s[j+1:]
    re=back(s)
    print(str(re-n)+' '+str(re))