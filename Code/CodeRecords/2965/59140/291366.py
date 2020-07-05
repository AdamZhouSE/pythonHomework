temp=input().split(" ")
k=int(temp[0])
m=int(temp[1])
s=input()
if len(s)>m:s=s[:m]
n=int(input())
for i in range(n):
    temp=input().split()
    a=int(temp[0])
    b=int(temp[1])
    c=int(temp[2])
    if c>=len(s):s=s+s[a:b]
    else:s=s[:c]+s[a:b]+s[c:]
    if len(s) > m: s = s[:m]
print(s[:k],end="")