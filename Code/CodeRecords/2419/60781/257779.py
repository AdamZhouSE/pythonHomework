n=input()
len=len(n)
n=list(map(int,n))
he=0
x=0
while x<len:
    he+=n[x]
    x+=1
x=0
ji=1
while x<len:
    ji*=n[x]
    x+=1
res=ji-he
print(res)