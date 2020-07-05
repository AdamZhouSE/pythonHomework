n=int(input())
s=input()
an=''
for i in range(len(s)):
    if (n+ord(s[i]))>ord('z'):
        an=an+chr(n+ord(s[i])-26)
    else:
        an=an+chr(n+ord(s[i]))
print(an,end='')