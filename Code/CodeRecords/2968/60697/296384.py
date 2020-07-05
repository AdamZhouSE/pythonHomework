s=input()
instrnum=int(input())
res=[]
for i in range(instrnum):
    res.append(input().split(' '))
def ishuiwen(s):
    leng=len(s)
    if(leng==0):
        return False
    half=leng//2
    for i in range(half):
        if(s[i]!=s[leng-1-i]):
            return False
    return True
end=0
ans=0
def addans(s,end):
    global ans
    for i in range(len(s)):
        for j in range(end,len(s)):
            if(ishuiwen(s[i:j+1])):
                ans+=1
addans(s,end)
for i in range(instrnum):
    k=res[i][0]
    if(k=='1'):
        end=len(s)
        s=s+res[i][1]
        addans(s,end)
    elif(k=='2'):
        s = res[i][1][::-1]+s
        for j in range(0,len(res[i][1])):
            for m in range(0,len(s)):
                if(ishuiwen(s[j:m+1])):
                    ans+=1
    elif(k=='3'):
        print(ans)




