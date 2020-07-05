def check(n,s):
    end,cnt,oddNum=n-1,0,0
    for i in range(end):
        for j in range(end,i-1,-1):
            if(i==j):
                if(n%2==0 or oddNum==1):
                    print('Impossible')
                    return
                oddNum=1
                cnt+=n//2-i
            elif(s[i]==s[j]):
                for k in range(j,end):
                    s[k],s[k+1]=s[k+1],s[k]
                end-=1
                break
    print(cnt)                
n=int(input())
while(True):
    s=input()
    if(s!=''):
        s=list(s)
        break
check(n,s)
