s=input()
s=s[1:len(s)-1].split(",")
n=int(input())
for i in range(len(s)):
    s[i]=int(s[i])
try:
    print(s.index(n))
except ValueError:
    print(-1)
