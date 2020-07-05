from fractions import Fraction
string=eval(input())
res=Fraction(string).limit_denominator(10)
print(res)