s=input()
s=s[1:len(s)-1].split(",")
anw=[]
for i in range(len(s)):
    s[i]=int(s[i])
for i in s:
    if s.count(i)>int(len(s)/3):
        anw.append(i)
print(list(set(anw)))