def Test():
    number=int(input())
    roman={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
    n=len(str(number))-1
    line=[]
    while(n>=0):
        line.append(int(str(number)[-1-n])*pow(10,n))
        n=n-1
    result=""
    for x in line:
        if(x==0):
            continue
        if(special(x)):
            result=result+roman[x]
        else:
            base=int(str(x).replace(str(x)[0],"1"))
            if(str(x)[0]=="2" or str(x)[0]=="3"):
                while(x!=0):
                    result=result+roman[base]
                    x=x-base
            else:
                five=int(str(x).replace(str(x)[0],"5"))
                result=result+roman[five]
                x=x-five
                while (x != 0):
                    result = result + roman[base]
                    x = x - base
    print(result)


def special(x):
    if(str(x)[0]=="1" or str(x)[0]=="4" or str(x)[0]=="5" or str(x)[0]=="9"):
        return True
    return False
if __name__ == "__main__":
    Test()