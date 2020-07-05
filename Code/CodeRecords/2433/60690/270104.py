str=input()[2:-2]
str=str.split("],[")
list=[]
for i in range(len(str)):
    l=str[i].split(",")
    l[0]=int(l[0])
    l[1]=int(l[1])
    list.append(l)
for i in range(len(list)-1):
    if list[i]==[0,0][:]: continue
    for j in range(i+1,len(list)):
        if list[j]==[0,0][:]: continue
        a,b,c,d=list[i][0],list[i][1],list[j][0],list[j][1]
        if a<c and b>=c and b<d:
            list[i][1]=list[j][1]
            list[j]=[0,0]
        elif c<a and d>=a and d<b:
            list[j][1]=list[i][1]
            list[i]=[0,0]
        elif a<=c and b>=d:
            list[j]=[0,0]
        elif c<=a and d>=b:
            list[i]=[0,0]
while [0,0] in list: list.remove([0,0])
print(list)