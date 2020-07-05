n=int(input())
s=bin(n)[2:]
t="0b"
for i in range(len(s)):
    if s[i]=='0':
        t+='1'
    else:
        t+='0'
print(int(t,2))