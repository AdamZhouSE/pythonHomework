t=int(input())
for i in range(0,t):
    n=int(input())
    s=list(str(bin(n)[2:len(str(bin(n)))]))
    for j in range(0,len(s)):
        if(s[j]=='1'):
            s[j]=0
        else:
            s[j]=1
    result=''
    for j in range(0,len(s)):
        result+=str(s[j])
    print(int(result,2))