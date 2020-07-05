time=int(input())
dict={
    'A':'2',
    'B':'2',
    'C':'2',
    'D':'3',
    'E':'3',
    'F':'3',
    'G':'4',
    'H':'4',
    'I':'4',
    'J':'5',
    'K':'5',
    'L':'5',
    'M':'6',
    'N':'6',
    'O':'6',
    'P':'7',
    'R':'7',
    'S':'7',
    'T':'8',
    'U':'8',
    'V':'8',
    'X':'9',
    'Y':'9',
    'Z':'9'
}
newList=[]
while(time>0):
    time-=1
    string=input()
    string=string.replace("-","")
    
    newString=""
    for c in string:
        if("0"<=c)and(c<="9"):
            newString+=c
        else:
            newString+=dict[c]
    newString=newString[:3]+'-'+newString[3:]
    newList.append(newString)

newList.sort()
length=len(newList)
listC=[1]*length
four=False
for i in range(length-1):
    if(newList[i]==newList[i+1]):
        listC[i]+=1

for i in range(length-2):
    if(newList[i]==newList[i+1])and(newList[i+1]==newList[i+2]):
        four=True
        break
        
for i in range(length):
    if(listC[i]!=1)and(not four):
        print(newList[i]+" "+str(listC[i]))
    if(listC[i]!=1)and(four):
        print(newList[i]+" "+str(4))
        break
none=True
for n in listC:
    if(n!=1):
        none=False
if(none):
    print("No duplicates.",end="")
            
    time=int(input())
while(time>0):
    time-=1
    string=input()
    string=string.replace("-","")