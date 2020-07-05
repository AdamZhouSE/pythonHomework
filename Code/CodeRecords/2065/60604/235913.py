        
def isdig(a):
    if a=='0' or a=='1' or a=='2' or a=='3' or a=='4' or a=='5' or a=='6' or a=='7' or a=='8' or a=='9':
        return True
    else:
        return False
def f(str):
    res=""
    i=0
    while(i<len(str)):
        while(True):
            if str[i]=='-' or isdig(str[i]):
                res+=str[i]
                i+=1
              
                break
            elif str[i]!=' ':
                return "0"
            i+=1
        while(True):
            if  not isdig(str[i]):
                i=len(str)
                
            else:
                
                res+=str[i]
                i+=1
                if (i==len(str)):
                    break
    return res
str=input()
if int(f(str))<-2147483648:
    print("-2147483648")
else:
    print(f(str))