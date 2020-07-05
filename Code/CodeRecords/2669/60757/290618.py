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
def caland(a,b):
    s1=cal(a)
    s2=cal(b)
    if len(s1)>len(s2):
        for j in range(len(s1)-len(s2)):
            s2='0'+s2
    elif len(s2)>len(s1):
        for j in range(len(s2)-len(s1)):
            s1='0'+s1
    re=''
    for i in range(len(s1)):
        if s1[i]=='1' and s2[i]=='1':
            re=re+'1'
        else:
            re=re+'0'
    return(back(re))
t=int(input())
for i in range(t):
    n=int(input())
    re=[]
    for j in range(n+1):
        if caland(j,n)==j:
            re.append(j)
    re=sorted(re)[::-1]
    for j in range(len(re)):
        print(re[j],end=' ')
    print()