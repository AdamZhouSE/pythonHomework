n=int(input())
s=input()
count=0
for i in range(len(s)):
    if s[i]=='0':
        count=count+1
str='1'
for i in range(count):
    str=str+'0'
print(str,end='')
        