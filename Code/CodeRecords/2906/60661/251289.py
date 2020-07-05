n=int(input())
s=input()
res=''
for i in range(len(s)):
    res+=chr((ord(s[i])+n-ord('a'))%26+ord('a'))
print(res,end='')