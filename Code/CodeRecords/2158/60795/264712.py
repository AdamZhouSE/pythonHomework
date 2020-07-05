import sys
sys.path.append('../')
import string

str=input()
result=[]
for i in range(0,len(str)):
    a=str[i]
    if a=='-':
        result.append('-')
    elif a=='1' or a=='2' or a=='0' or a=='3' or a=='4' or a=='5' or a=='6' or a=='7' or a=='8' or a=='9':
        result.append(a)
    else:
        continue
if len(result)==0:
    print(0)
else:
    arr="".join(result)
    re=int(arr)
    if re>2147483648:
        re=2147483648
    if re<-2147483648:
        re=-2147483648
    print(re)