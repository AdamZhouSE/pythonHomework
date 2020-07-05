spe={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
val={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
number=input()
result=0
if number in spe:
    result=spe[number]
else:
    token=[ch for ch in number]
    i=0
    while i <len(token):
        if i<len(token)-1:
            if token[i] + token[i + 1] in spe:
                result = result + spe[token[i] + token[i + 1]]
                i = i + 2
            else:
                result = result + val[token[i]]
                i = i + 1
        else:
            result = result + val[token[i]]
            i=i+1

print(result)