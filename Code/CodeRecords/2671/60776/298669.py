a=int(input())
for k in range(0,a):
    a=int(input())
    str=""
    result=0
    for i in range(0,a):
        str=str+"1"
    a=int(str,2)
    for i in range(0,a+1):
        str=bin(i).replace("0b","")
        for j in range(0,len(str)-1):
            if str[j]=='1' and str[j+1]=='1':
                result=result+1
                break
    print(result)