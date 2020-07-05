str=input()
print(str)
str=str.replace("dividend = ","")
str=str.replace(" divisor = ","")
list=str.split(",")
if len(list)==1:
    print(str)
else:
    a=int(list[0])
    b=int(list[1])
    result=int(a/b)
    print(result)