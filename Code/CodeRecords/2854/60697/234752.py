sizes=list(map(int,input().split(' ')))
tmp=[]
for i in range(len(sizes)):
    num=sizes.count(sizes[i])
    if(num==4):
        leg=sizes[i]
    elif(num==5):
        print("Bear")
        break
    elif(num==6):
        print("Elephant")
        break
    else:
        tmp.append(sizes[i])
if(len(tmp)>2):
    print("Alien")
elif (len(tmp)==2):
    if(tmp[0]!=tmp[1]):
        print("Bear")
    else:
        print("Elephant")
        
