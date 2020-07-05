n=int(input())
s=list(input())

for i in range(len(s)):
    s[i]=chr(ord('a')+((ord(s[i])+n-ord('a'))%26))

print(''.join(s),end='')