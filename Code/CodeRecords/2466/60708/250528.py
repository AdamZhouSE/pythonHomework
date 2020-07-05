def team(temp):
    listbig=[]
    for x in range(0,len(temp)+1-3):
        i=temp[x]
        for y in range(x+1,len(temp)+1-2):
            j=temp[y]
            for z in range(y+1,len(temp)+1-1):
                k=temp[z]
                listsmall = []
                listsmall.append(i)
                listsmall.append(j)
                listsmall.append(k)
                listbig.append(listsmall)
    return listbig
def check(list):
    result=0
    for item in list:
        x=item[0]+item[1]
        y=item[1]+item[2]
        z=item[0]+item[2]
        if(item[2]<x and item[0]<y and item[1]<z):
            result=result+1
    return result
nfq=int(input())
n=[]
Str=[]
for i in range(0,nfq):
   n.append(int(input()))
   Str.append(input())
for i in range(0,nfq):
    temp1=Str[i].split(" ")
    temp2=[]
    for item in temp1:
        temp2.append(int(item))
    list=[]
    list=team(temp2)
    print(check(list))