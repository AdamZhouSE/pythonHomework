s=input().split(',')
max=1
for i in range(0,len(s)-1):
    temp=int(s[i])
    length=1
    for j in range(i+1,len(s)):
        if int(s[j])>temp:
            temp=int(s[j])
            length=length+1
    if length>max:
        max=length
print(max)