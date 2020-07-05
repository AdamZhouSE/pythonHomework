n=int(input())
s=input()
temp=""
for i in range(0,len(s)):
    temp=temp+chr(ord(s[i])+n%26)
print(temp,end="")