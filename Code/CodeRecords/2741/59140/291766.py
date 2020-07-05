s=input()
s=s[1:len(s)-1].split(",")
maxlen=0
length=0
p=0
for i in range(len(s)):
    if int(s[i])>p:
        p=int(s[i])
        length+=1
        if length>maxlen:maxlen=length
    else:
        p=int(s[i])
        length=1
print(maxlen)