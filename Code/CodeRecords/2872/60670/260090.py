n=int(input())
s=input()
l=len(s)
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        l-=1
print(len(s)-l)