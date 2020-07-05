number=int(input(""))
card=raw_input("").split(" ")
list=[]
for i in range(number):
    list.append(int(card[i]))
saileijia=0
dima=0
while(len(list)!=0):
    if(list[0]>list[-1]):
        saileijia=saileijia+list[0]
        list.pop(0)
    else:
        saileijia=saileijia+list[-1]
        list.pop(-1)
    if(len(list)==0):
        break;
    if(list[0]>list[-1]):
        dima=dima+list[0]
        list.pop(0)
    else:
        dima=dima+list[-1]
        list.pop(-1)
print(str(saileijia)+" "+str(dima))