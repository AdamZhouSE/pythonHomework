def intToBi(x):
    temp=""
    while(x>1):
        temp=str(x%2)+temp
        x=x//2
    temp=str(x)+temp
    return temp

def biToInt(bistr):
    result=0
    for i in range(0,len(bistr)):
        if bistr[i]=='1':
            result=result+pow(2,len(bistr)-1-i)
    return result

t=eval(input())
for i in range(0,t):
    x=eval(input())
    str1=intToBi(x)
    str2=""
    for j in range(0,len(str1)):
        if str1[j]=="0":
            str2=str2+"1"
        else:
            str2=str2+"0"
    result=biToInt(str2)
    print(result,end=' ')
    print(x+result)