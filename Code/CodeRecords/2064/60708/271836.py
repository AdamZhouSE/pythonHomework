# I， V， X， L，C，D和M
str=input()
result=0
k=-1
while(True):
    if ("CM" in str):
        result = result + 900
        str = str.replace("CM", "")
    elif ("CD" in str):
        result = result + 400
        str = str.replace("CD", "")
    elif ("XL" in str):
        result = result + 40
        str = str.replace("XL", "")
    elif ("XC" in str):
        result = result + 90
        str = str.replace("XC", "")
    elif ("IX" in str):
        result = result + 9
        str = str.replace("IX", "")
    elif ("IV" in str):
        result = result + 4
        str = str.replace("IV", "")
    else:
        break
for item in str:
    if(item=='M'):
        result=result+1000
    if(item=='D'):
        result=result+500
    if(item=='C'):
        result=result+100
    if(item=='L'):
        result=result+50
    if(item=='X'):
        result=result+10
    if(item=='V'):
        result=result+5
    if(item=='I'):
        result=result+1
print(result)