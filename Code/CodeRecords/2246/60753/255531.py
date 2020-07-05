import math
n=input()
listnum=list(str(n))
listnum=sorted(listnum,reverse =1)
strn="".join(listnum)
mi=0
isTrue=0
while int(math.pow(2,mi))<=int(strn):
    judge=int(math.pow(2,mi))
    judnum=list(str(judge))
    judnum=sorted(judnum,reverse =1)
    strjud="".join(judnum)
    if strn==strjud:
        isTrue=1
        break
    else:
        mi+=1
if isTrue==0:
    print("False")
else:
    print("True")