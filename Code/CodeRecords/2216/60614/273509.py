from fractions import Fraction
result=Fraction(eval(input())).limit_denominator()
if result==int(result):
    print(str(result)+'/1')
else:
    print(result)