n=int(input())
s=input()
res=0
for i in range(n):
    if s[i]=='A':
        res+=4
    elif s[i]=='B':
        res+=3
    elif s[i]=='C':
        res+=2
    elif s[i]=='D':
        res+=1
if res==0:
    print(0,end="")
else:
    print("%.14f" % (4 * res / (n * 4)), end="")