string=input()
temp=list(string)
sum=0
if "IV" in string:
    sum+=4
    del temp[temp.index("I")]
    del temp[temp.index("V")]
if "IX" in string:
    sum+=9
    del temp[temp.index("I")]
    del temp[temp.index("X")]
if "XL" in string:
    sum+=40
    del temp[temp.index("L")]
    del temp[temp.index("X")]
if "XC" in string:
    sum+=90
    del temp[temp.index("C")]
    del temp[temp.index("X")]
if "CD" in string:
    sum+=400
    del temp[temp.index("C")]
    del temp[temp.index("D")]
if "CM" in string:
    sum+=900
    del temp[temp.index("C")]
    del temp[temp.index("M")]
while temp!=[]:
    if "I" in temp:
        sum+=1
        del temp[temp.index("I")]
    if "V" in temp:
        sum+=5
        del temp[temp.index("V")]
    if "X" in temp:
        sum+=10
        del temp[temp.index("X")]
    if "L" in temp:
        sum+=50
        del temp[temp.index("L")]
    if "C" in temp:
        sum+=100
        del temp[temp.index("C")]
    if "D" in temp:
        sum+=500
        del temp[temp.index("D")]
    if "M" in temp:
        sum+=1000
        del temp[temp.index("M")]
print(sum)