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
def calor(a,b):
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
        if s1[i]=='1' or s2[i]=='1':
            re=re+'1'
        else:
            re=re+'0'
    return(back(re))
t=int(input())
for i in range(t):
    li=input().split()
    n=int(li[0])
    x=int(li[1])
    li=list(map(int,input().split()))
    re=[]
    for j in range(len(li)):
        if li[j]%x==0:
            re.append(li[j])
    if(len(re)==0):
        print('0')
    elif(len(re)==1):
        print(re[0])
    else:
        c=len(re)
        for j in range(c-1):
            re[0]=calor(re[0],re[1])
            del re[1]
        print(re[0])