str1=input()
list1=str1.split()
listtnum=list1[2][1:-2]
listnumm=listtnum.split(",")
listnum=[]
for x in listnumm:
    listnum.append(int(x))
k=int(list1[5][0])
t=int(list1[8])
isHave=False
length=len(listnum)
for i in range(length-1):
    for j in range(i+1,length):
        if(abs(listnum[i]-listnum[j])<=t)and(abs(i-j)<=k):
            isHave=True
if(isHave):
    print("true")
else:
    print("false")
