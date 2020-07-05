s=input().split(',')
h=0
for i in range(0,len(s)):
    if int(s[i])>=len(s)-i-1:
        h=int(s[i])
        break
print(h)