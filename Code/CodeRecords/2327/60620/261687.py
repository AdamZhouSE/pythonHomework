s=input()
a=[i for i in range(len(s)+1)]
result=[]
for i in range(len(s)):
    if(s[i]=='I'):
        result.append(a[0])
        a.remove(a[0])
    if(s[i]=='D'):
        result.append(a[-1])
        a.remove(a[-1])
result.append(a[0])
print(result)