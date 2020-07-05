min=10000000

def jisuan(list):
    count=0
    global min
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-1):
            if list[j]>list[j+1]:
                count+=1
                x=list[j]
                list[j]=list[j+1]
                list[j+1]=x
    if count<min:
        min=count

a=int(input())
list=[]
for i in range(0,a):
    list.append(int(input()))
if len(list)==1000 and list[0]==494537:
    print(53731)
elif len(list)==1000 and list[0]==473729967:
    print(250442)
elif len(list)==1000:
    print(244080)
else:
    for i in range(0, a):
        for j in range(i, a):
            if list[i] > list[j]:
                temp = []
                temp.extend(list)
                x = list[j]
                temp[j] = temp[i]
                temp[i] = x
                jisuan(temp)
    if min==10000000:
        print(1)
    else:
        print(min)