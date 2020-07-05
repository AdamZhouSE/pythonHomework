def findabc(s,letter):
    ans=0
    #print(s,letter)
    if(letter=='c'):
        n=s.count('c')
        ans=int(pow(2,n)-1)
        return ans
    if(len(s)==0):
        return ans
    elif(letter=='b'):
        if('b' in s):
            i=s.index('b')
            ans+=2*findabc(s[i+1:],'b')
            ans+=findabc(s[i+1:],'c')
        return ans
    elif(letter=='a'):
        if('a' in s):
            i=s.index('a')
            ans+=2*findabc(s[i+1:],'a')
            ans+=findabc(s[i+1:],'b')
        return ans

t=int(input())
for i in range(t):
    s=input()
    while(len(s)>0 and s[0]!='a'):
        s=s[1:]
    while(len(s)>0 and s[-1]!='c' ):
        s=s[:-1]
    res=findabc(s,'a')
    print(res)