s=input()
result=[]
if s[0]==s[1]:
    result.append(1)
    n=2
else:
    n=1
for i in range(n,len(s)):
    if s[i]<s[i-1]:
        result.append(i)
result.append(len(s))
for i in range(len(result)):
    if i<len(result)-1:
        print(result[i],end=' ')
    else:
        print(result[i],end="")





