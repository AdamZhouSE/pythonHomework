a=input()
a=a.replace("[[","")
a=a.replace("]]","")
a=a.replace(" ","")
b=a.split("],[")
for i in range(0,len(b)):
    b[i]=b[i].replace("\"","")
    b[i]=b[i].split(",")
list=["JFK"]
dangqian="JFK"
qishizhan=[]
for i in range(0,len(b)):
    qishizhan.append(b[i][0])
while(dangqian in qishizhan):
    temp=[]
    for i in range(0,len(b)):
        if b[i][0]==dangqian:
            temp.append(b[i][1])
    temp.sort()
    list.append(temp[0])
    for i in range(0,len(b)):
        if b[i][0]==dangqian and b[i][1]==temp[0]:
            del b[i]
            break
    qishizhan.remove(dangqian)
    dangqian=temp[0]
print(list)