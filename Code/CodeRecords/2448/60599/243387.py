s=list(eval(input()))
s.sort()
maxH=1
for i in range(len(s)):
    if(len(s)-i==s[i]):
        maxH=max(s[i],maxH)
print(maxH)