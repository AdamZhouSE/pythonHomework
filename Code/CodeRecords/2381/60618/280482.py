a=[int(n) for n in input().split(",")]
a.reverse()
b=[int(n) for n in input().split(",")]
b.reverse()
rea,reb=0,0
for i in range(0,len(a)):
    rea+=a[len(a)-i-1]*((-2)**i)
for i in range(0,len(b)):
    reb+=b[len(b)-i-1]*((-2)**i)
print(rea+reb)