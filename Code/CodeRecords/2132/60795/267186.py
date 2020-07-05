def clean(ch,str1):
    sstr=list(str1)
    for i in range(0,len(sstr)):
        if sstr[i]==ch:
            sstr[i]='0'
            break
    sstr="".join(sstr)
    return sstr

str=input()
result=[]
for i in range(0,len(str)):
    if str[i]=='z': #0 zero
        str=clean('z',str)
        str=clean('e',str)
        str=clean('r',str)
        str=clean('o',str)
        result.append('0')
    elif str[i]=='w': #2 two
        str=clean('w',str)
        str=clean('t',str)
        str=clean('o',str)
        result.append('2')
    elif str[i]=='u': #4 four
        str=clean('u',str)
        str=clean('f',str)
        str=clean('o',str)
        str=clean('r',str)
        result.append('4')
    elif str[i]=='x': #6 six
        str=clean('x',str)
        str=clean('s',str)
        str=clean('i',str)
        result.append('6')
    elif str[i]=='g': #8 eight
        str=clean('g',str)
        str=clean('e',str)
        str=clean('i',str)
        str=clean('h',str)
        str=clean('t',str)
        result.append('8')
    elif str[i]=='0':
        continue
# one  three  five  seven  nine
for i in range(0,len(str)):
    if str[i]=='o':  #1 one
        str=clean('o',str)
        str=clean('n',str)
        str=clean('e',str)
        result.append('1')
    elif str[i]=='t': #3 three
        str=clean('t',str)
        str=clean('h',str)
        str=clean('r',str)
        str=clean('e',str)
        str=clean('e',str)
        result.append('3')
    elif str[i]=='f': #5 five
        str=clean('f',str)
        str=clean('i',str)
        str=clean('v',str)
        str=clean('e',str)
        result.append('5')
    elif str[i]=='s': #7 seven
        str=clean('s',str)
        str=clean('e',str)
        str=clean('v',str)
        str=clean('e',str)
        str=clean('n',str)
        result.insert('7')
    elif str[i]=='0':
        continue
for i in range(0,len(str)):
    if str[i]=='0':
        continue
    else:
        result.append('9')
        break
for i in range(0,len(result)):
    for j in range(i+1,len(result)):
        if result[i]>result[j]:
            result[i],result[j]=result[j],result[i]
res=""
for i in range(0,len(result)):
    res=res+result[i]
print(res)