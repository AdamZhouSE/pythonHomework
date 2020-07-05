N=int(input())
minStr,minLen=0,256
string=[]
for i in range(N):
    sss=input().strip()
    string.append(sss)
    if(len(sss)<minLen):
        minLen=len(sss)
        minStr=i
dest,ans,maxx='','',0
for i in range(minLen):
    for j in range(minLen-i):
        dest=string[minStr][i:i+j]
        ok=True
        for k in range(N):
            if(dest not in string[k]):
                ok=False
                break
        if(ok and len(dest)>maxx):
            maxx=len(dest)
            ans=dest
print(maxx)

