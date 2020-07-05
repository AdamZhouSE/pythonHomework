s=input()
for i in range(0,len(s)):
    if s[i]>='0' and s[i]<='9':
        temp=''
        while s[i]>='0' and s[i]<='9':
            temp=temp+s[i]
            i=i+1
        num1=int(temp)
    