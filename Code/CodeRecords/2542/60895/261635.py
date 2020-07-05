s=input().lstrip('[')
s=s.rstrip(']')
s=s.split(',')
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if int(s[i])>int(s[j]):
            s[i],s[j]=s[j],s[i]
max=1
for m in range(0,len(s)-1):
    if int(s[m+1])-int(s[m])==1:
        length=2
        for n in range(m+1,len(s)-1):
            if int(s[n+1])-int(s[n])==1:
                length=length+1
            else:
                break
        if length>max:
            max=length
print(max)