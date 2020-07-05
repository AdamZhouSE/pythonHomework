s=input()
re=0
length=0
str=''
for i in range(0,len(s)):
    for j in range(i,len(s)):
        if s.count(s[i:j+1])>=re and length<=(j-i+1):
            re=s.count(s[i:j+1])
            length=j-i+1
            str=s[i:j+1]
print(str)