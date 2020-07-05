

token=[{1:'I',5:'V',4:'IV',9:'IX'},{1:'X',5:'L',4:'XL',9:'XC'},{1:'C',5:'D',4:'CD',9:'CM'},{1:'M'}]
number=[int(i) for i in input()]
result=''
number.reverse()
bits=len(number)
for i in range(len(number)-1,-1,-1):
    if number[i]==0:
        continue
    elif number[i]==9:
        result=result+token[i][9]
        continue
    elif number[i]>=5:
        result=result+token[i][5]
        for j in range(0,number[i]-5):
            result=result+token[i][1]
        continue
    elif number[i]==4:
        result=result+token[i][4]
        continue
    else:
        for j in range(0,number[i]):
            result=result+token[i][1]
        continue

print(result)