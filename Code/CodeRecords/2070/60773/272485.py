import math
n1=float(input())
#print(n1)
n2=int(input())
#print(n2)
str=str(pow(n1,n2))
for i in range(len(str)):
    if str[i]=='.':
        s=str[i+1:]
        s1=str[:i+1]
        break
if len(s)<5:
    for i in range(5-len(s)):
        s=s+"0"
else:
    s=s[:5]
print(s1+s)
    