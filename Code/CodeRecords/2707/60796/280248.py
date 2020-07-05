s=input()
s=s[1:len(s)-1]
ls=s.split(",")
ls=[int(x) for x in ls]
n=0
i=0
while i<=len(ls)-2:
    if ls[i]%2==0:
        j=ls[i]+1
    else:
        j=ls[i]-1
    if ls[i+1]!=j:
        n=n+1
        for m in range(i+2,len(ls)):
            if ls[m]==j:
                ls[i+1],ls[m]=ls[m],ls[i+1]
                break
    i=i+2
print(n)