import math
l=int(input())
r=int(input())
res=0
for i in range(l,r+1):
    s=str(i)
    p=True
    for j in range(0,len(s)):
        if s[j:j+1]!=s[len(s)-j-1:len(s)-j]:
            p=False
            break
    if p and int(math.pow(i,1/2)*1000)%1000==0:
        s=str(int(math.pow(i,1/2)))
        p1=True
        for j in range(0, len(s)):
            if s[j:j + 1] != s[len(s) - j - 1:len(s) - j]:
                p1 = False
                break
        if p1:
            
            res=res+1
print(res)
