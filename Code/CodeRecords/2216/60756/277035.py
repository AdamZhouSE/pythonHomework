import math
s=list(input())
i=1
while i<len(s):
    if s[i]=='-':
        s.insert(i,'+')
        i+=1
    i+=1
s=''.join(s).split("+")
arr=[]
for i in range(len(s)):
    arr.append(list(map(int,s[i].split("/"))))
numerator=0
denominator=1
for i in arr:
    LCM=denominator*i[1]//math.gcd(denominator,i[1])
    numerator=(LCM//denominator)*numerator+(LCM//i[1])*i[0]
    denominator=LCM
    GCD=math.gcd(denominator,numerator)
    denominator//=GCD
    numerator//=GCD
print("%d/%d" %(numerator,denominator))