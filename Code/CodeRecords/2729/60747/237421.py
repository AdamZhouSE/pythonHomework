s=input()
s=s[1:len(s)-1].split(",")
for i in range(len(s)):
    s[i]=int(s[i])
for i in s:
    if s.count(i)==1 :
        print(i)