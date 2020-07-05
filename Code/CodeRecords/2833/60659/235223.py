n=int(input())
a=input().split(" ")
b=input().split(" ")
for i in range(n):
    a[i]=int(a[i])
    b[i]=int(b[i])
    if a[i]>b[i]:
        result="NO"
b.sort()
sun=0
for j in a:
    sun+=j
if b[len(b)-1]+b[len(b)-2]-sun>=0:
    result="YES"
else:
    result="NO"
print(result)
    