s0=input()
n=int(input())
i=0
while i<n:
    s=input()
    if(s[0]=='1'):
        s0=s0+s[2:]
        i+=1
        continue
    if(s[0]=='2'):
        s=list(s[2:])
        s.reverse()
        s=''.join(s)
        s0=s+s0
        i+=1
        continue

    if(s[0]=='3'):
        count = 0
        lenth=len(s0)
        if(lenth==1):
            print('1')
        else:
            count=lenth
            j=0
            x=1
            while j+x<lenth:
                while j + x < lenth:
                    temp=s0[j:j+x+1]
                    newtemp=list(temp)
                    newtemp.reverse()
                    newtemp=''.join(newtemp)
                    if(temp==newtemp):
                        count+=1
                    j+=1
                x+=1
                j=0
            print(count)
    i+=1
