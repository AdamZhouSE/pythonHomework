num=int(input())
def solve(s):
    res=[]
    for i in range(len(s)):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
            for j in range(len(s)-1,i,-1):
                if s[j]!='a' and s[j]!='e' and s[j]!='i' and s[j]!='o' and s[j]!='u':
                    sub=s[i:j+1]
                    res.append(sub)
                    for k in range(1,len(sub)-1):
                        solve(s)
    return res
    
for i in range(num):
    s=str(input())
    res=solve(s)
    if len(res)==0:
        print('-1')
    else:
        for j in res:
            if j!=res[-1]:
                print(j,end=" ")
            else:
                print(j)
    