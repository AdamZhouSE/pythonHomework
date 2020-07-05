from scipy.special import comb, perm
number=int(input(""))
list=[]
list.append(input("").split(" "))
list.append(input("").split(" "))
card_1=[]
card_2=[]
for i in range(int(list[0][0])):
    card_1.append(int(list[0][i+1]))
for i in range(int(list[1][0])):
    card_2.append(int(list[1][i+1]))
card_number=int(list[0][0])+int(list[1][0])
max_time=int(perm(card_number,card_number))
time=0
while(max_time>time):
    if(card_1[0]>card_2[0]):
        a=card_1[0]
        card_1.pop(0)
        card_1.append(card_2[0])
        card_2.pop(0)
        card_1.append(a)
    else:
        a=card_2[0]
        card_2.pop(0)
        card_2.append(card_1[0])
        card_1.pop(0)
        card_2.append(a)
    time=time+1
    if(len(card_1)==0):
        print(str(time)+" 2")
        break
    elif(len(card_2)==0):
        print(str(time)+" 1")
        break
if(max_time==time):
    print(-1)
    