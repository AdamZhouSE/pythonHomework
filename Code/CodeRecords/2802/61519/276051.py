num=list(input().split(" "))
human=list(input().split(" "))
human2=[]
candy=int(num[1])
for i in range(int(num[0])):
    human2.append(i+1)
    human[i]=int(human[i])
while len(human)>0:
    if human[0]>candy:
        human.append(human[0]-candy)
        human.remove(human[0])
        human2.append(human2[0])
        human2.remove(human2[0])
    else:
        human.remove(human[0])
        human2.remove(human2[0])
    if len(human2)==1:
        print(human2[0])
        break