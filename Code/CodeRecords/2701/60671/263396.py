import re
list1=input()
list22=re.findall(r"\d",list1)
list2=[]
for i in list22:
    list2.append(int(i))
length=len(list2)
chess=[[0]*3]*3
listA=[]
listB=[]
for i in range(int(length/2)):
    if(i%2==0):
        listA.append(str(list2[2*i])+str(list2[2*i+1]))
    else:
        listB.append(str(list2[2*i])+str(list2[2*i+1]))

winCheck=[["00","11","22"],["20","11","02"],["00","01","02"],["10","11","12"], ["20","21","22"], ["00","10","20"],["01","11","21"], ["02","12","22"]]   

aWin=False
bWin=False
for x in winCheck:
    if(x[0] in listA)and(x[1] in listA)and(x[2] in listA):
        aWin=True
        break
for x in winCheck:
    if(x[0] in listB)and(x[1] in listB)and(x[2] in listB):
        bWin=True
        break
if(aWin)and(not bWin):
    print('A')
elif(bWin)and(not aWin):
    print('B')
else:
    if(len(list2)==18):
        print("Draw")
    else:
        print("Pending")
