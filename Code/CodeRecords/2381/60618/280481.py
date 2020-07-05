a=[int(n) for n in input().split(",")]
a.reverse()
b=[int(n) for n in input().split(",")]
b.reverse()
rea,reb=0,0
for i in range(0,len(a)):
    rea+=a[n-i]*((-2)**i)
for i in range(0,len(b)):
    reb+=b[n-i]*((-2)**i)
print(rea+reb)