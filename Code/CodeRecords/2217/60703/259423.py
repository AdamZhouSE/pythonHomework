list1 = [int(x) for x in input().split(",")]
list2 = [int(x) for x in input().split(",")]
list3 = [int(x) for x in input().split(",")]
list4 = [int(x) for x in input().split(",")]


x1,y1 = list1[0],list1[1]
x2,y2 = list2[0],list2[1]
x3,y3 = list3[0],list3[1]
x4,y4 = list4[0],list4[1]

def length(x1,y1,x2,y2):
    return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)


len12 = length(x1,y1,x2,y2)
len13 = length(x1,y1,x3,y3)
len14 = length(x1,y1,x4,y4)
len23 = length(x2,y2,x3,y3)
len24 = length(x2,y2,x4,y4)
len34 = length(x3,y3,x4,y4)


LIST =[]
LIST.append(len12)
LIST.append(len13)
LIST.append(len14)
LIST.append(len23)
LIST.append(len24)
LIST.append(len34)

LIST.sort()
if(
    LIST[0]==LIST[1] and
    LIST[0]==LIST[2] and
    LIST[0]==LIST[3] and
    LIST[4] == 2*LIST[0] and
    LIST[4]==LIST[5]
):
    print(True)
else:
    print(False)
