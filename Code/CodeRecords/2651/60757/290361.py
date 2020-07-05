t=int(input())
for i in range(t):
    a=int(input())
    s=''
    while(a!=0):
        if a%2==1:
            s='1'+s
        else:
            s='0'+s
        a=a//2
    if len(s)%2==1:
        s='0'+s
    for j in range(int(len(s)/2)):
        s=s[:2*j]+s[2*j+1]+s[2*j]+s[2*j+2:]
    re=0
    for j in range(len(s)):
        re=re*2
        re+=ord(s[j])-ord('0')
    print(re)