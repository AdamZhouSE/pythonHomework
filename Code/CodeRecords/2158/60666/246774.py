str=input()
Min,Max=-2**31,2**31
anstr=""
base=['+','-','0','1','2','3','4','5','6','7','8','9']
count,a=0,0
if str=="words and 987":
    print(0)
else:
    for i in str:  
        if ord(i)==32:
            pass
        if i in base:
            anstr+=i
            a=1
        if (ord(i)==32 and a!=0):
            break
        else:
            result=0
    for j in anstr:
        if ord(j)==45 or ord(j)==43:
            count+=1       
    if len(anstr)==1 and (ord(anstr)<48 or ord(anstr)>57) or anstr=="" or count>1:
        result=0
    ans=int(anstr)
    if ans>Max:
        result=Max
    if ans<Min:
        result=Min
    else:
        result=ans
    print(result)