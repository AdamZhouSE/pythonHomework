num=int(input())
def solve(s):
    for i in range(len(s)):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':#如果是元音
            for j in range(len(s)-1,i-1,-1):
                if s[j]!='a' and s[j]!='e' and s[j]!='i' and s[j]!='o' and s[j]!='u':#如果是辅音
                    sub=s[i:j+1]
                    res.append(sub)
                    for k in range(1,len(sub)-1):
                        sb=sub[k:]
                        solve(sb)
    return res
    
for i in range(num):
    res=[]
    s=str(input())
    res=solve(s)
    if len(res)==0:
        print('-1')
    else:
        for j in range(len(res)):
            if j!=len(res)-1:
                print(res[j],end=" ")
            else:
                print(res[j])
    