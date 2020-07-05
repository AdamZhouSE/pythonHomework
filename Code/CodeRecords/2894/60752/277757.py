size=int(input())
s=input()
count=0
for i in range(len(s)-1):
    if s[i:i+2]=="VK":
        s=s[0:i]+"  "+s[i+2:]
        count+=1
for i in range(len(s)):
    if s[i]=='V':
        if i+1<len(s):
            if s[i+1]!=' ':
                count+=1
                break
    if s[i]=='K':
        if i!=0:
            if s[i-1]!=' ':
                count+=1
                break
print(count,end='')

