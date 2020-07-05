t=int(input())
for time in range(0,t):
    s=input()
    n1=int(s)
    for i in range(0,len(s)):
        if(s[i]=='6'):
            s=s[0:i]+"9"+s[i+1:]
    n2=int(s)
    print(n2-n1)