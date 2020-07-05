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
    s='0'+cal(n)
    re='0'
    for i in range(1,len(s)):
        if re[i-1]!=s[i]:
            re=re+'1'
        else:
            re=re+'0'
    print(back(re))
    
    