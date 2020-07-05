data=input("请输入一段加法表达式")
sub_string=a.split("+")
list=[]
for each in  sub_string:
    list.append(int(each))
    list.sort()
result=""
number=0
for ea in list:
    result=result+"+"+ea
    number+=ea
    
print(f"{result}={number}")
        