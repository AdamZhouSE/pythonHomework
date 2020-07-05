import math
string=input()
string=string[1:len(string)-1]
list1=string.split(",")

limit=math.floor(len(list1)/3)
resultlist=[]
count=0
for element in list(set(list1)):
    for i in list1:
        if i==element:
            count=count+1
            if count>limit:
                resultlist.append(element)
                break
    count=0
print(str(sorted(resultlist)).replace("'",''))