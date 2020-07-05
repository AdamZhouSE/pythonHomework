s=list(input())
s.sort()
l = []
sum1=0
pre=s[0]
s1=pre
for i in range(len(s)):
    if s[i]!=pre:
        l.append([s1,sum1])
        pre =s[i]
        s1=pre
        sum1=1
    else:
        sum1+=1
        s=s+pre
    if i==len(s)-1:
        l.append([s[i],sum1])
l.sort(key= lambda s:-s[1])
