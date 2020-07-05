from _pydecimal import Decimal

NUM,string=int(input()),input()
lst=[]
for i in range(NUM):
    if string[i]=="A" or string[i]=="a":
        lst.append(4)
    elif string[i]=="B" or string[i]=="b":
        lst.append(3)
    elif string[i]=="C" or string[i]=="c":
        lst.append(2)
    elif string[i] == "D" or string[i] == "d":
        lst.append(1)
    elif string[i]=="F" or string[i]=="f":
        lst.append(0)
    else:
        lst.append(0)
total=sum(lst)
if total==0:
    print(0,end="")
else:
    
    result=Decimal(str(total))/Decimal(str(NUM))
    print(format(result,"0.14f"),end="")

