n=int(input())
s=input().split()
diff,result=0,0
for i in range(n):
    s[i]=int(s[i])
s.sort()
test=[s[0]]
for i in range(n-1):
    if s[i+1]!=s[i]:
        test.append(s[i+1])
if len(test)>3:
    result=-1
elif len(test)==3:
    for i in range(n-1):
        if (diff!=0)&(s[i+1]-s[i]!=0)&(s[i+1]-s[i]!=diff):
            result=-1
            break
        else:
            diff=s[i+1]-s[i]
    else:
        result=diff
elif len(test)==2:
    result=s[-1]-s[0]
else:
    result=0
print(result)