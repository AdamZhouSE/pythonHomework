spe={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':1000}
number=input()
result=0
if number in spe:
    result=spe[number]
else:
    token=[ch for ch in number]
    result=token.count('I')*1+token.count('V')*5+token.count('X')*10+token.count('L')*50+token.count('C')*100+token.count('D')*500+token.count('M')*1000
print(result)