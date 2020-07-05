Str = input().split("=")
import re
pattern = re.compile(r'[+-]?[\d]*[x]?')
left = Str[0]
right = Str[1]

leftList = pattern.findall(left)
rightList = pattern.findall(right)

param = 0
num = 0
for i in leftList:
    if(i==""):
        continue
    if('x' in i):
        if(i=='x' or i=="+x"):
            param+=1
        elif(i=='-x'):
            param+=-1
        else:
            param+= int(i[:-1])
    else:
        num -= int(i)



for i in rightList:
    if(i==""):
        continue
    if('x' in i):
        if(i=='x' or i=="+x"):
            param-=1
        elif(i=='-x'):
            param-=-1
        else:
            param-= int(i[:-1])
    else:
        num += int(i)
if(param==0 and num==0):
    print("Infinite solutions")
elif(param==0):
    print("No solution")
else:
    x = num/param
    print("x="+str(x))
    
