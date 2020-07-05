from fractions import Fraction
string=eval(input())
res=Fraction(string).limit_denominator(10)
if(len(str(res))<3):
    print(str(res)+"/1")
else:
    print(res)
   