import fractions
n=input()
a=eval(n)
s=str(a).split('.')
res=''
if s[1].count('0')==len(s[1]):
    res=s[0]+'/1'
else:
    t=str(fractions.Fraction(a)).split('/')
    b=int(t[1])/int(t[0])
    c=1
    while(str(b).split('.')[1].count('0')!=len(str(b).split('.')[1])):
        c=c*2
        b=b*2
    res=(str(int(c))+'/'+str(int(b)))


print(res)

