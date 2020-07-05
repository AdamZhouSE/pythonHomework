def GCD(a,b):
    while b!=0:
        temp=a%b
        a,b=b,temp
    return a
def LCM(a,b):
    return (a*b//GCD(a,b))
import re
expression=input()
res=[]
s=re.findall(r'\d+/\d+',expression)
oprator=re.findall(r'\d([+-])\d',expression)
for item in s:
    res.append(list(map(int,(item.split("/")))))
min1=int(res[0][1])
for i in range(1,len(res)):
    min1=LCM(min1,(res[i][1]))
for i in range(len(res)):
    res[i][0]*=(min1//(res[i][1]))
k=(res.pop(0)[0])
k=-k if expression[0]=='-' else k
while oprator:
    opratori=oprator.pop(0)
    tmpstr=res.pop(0)
    k+=(tmpstr[0]) if opratori=='+' else -(tmpstr[0])
if k==0:
    print("0/1")
else:
    gcd=GCD(abs(k),min1)
    print('{0}/{1}'.format(k//gcd,min1//gcd))