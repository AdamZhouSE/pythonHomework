str=input()
str=str[1:-1]
list=str.split(",")
num=[]
for x in list:
    num.append(int(x))
north=num[0]
west=num[1]
south=num[2]
east=num[3]
if(north>=south)and(east>=west):
    print(True)
else:
    print(False)