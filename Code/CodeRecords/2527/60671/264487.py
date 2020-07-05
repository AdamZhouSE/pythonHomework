import re
string=input()

list0=[]

for x in string:
    if(x!="[")and(x!="]"):
        list0.append(x)
str0="".join(list0)
#print(str0)

list22=str0.split(",")
#print(list22)

list2=[]
for i in list22:
    list2.append(int(i))

alll=len(list2)
length=int(alll/5)

idi=[0]*length
ratingi=[0]*length
veganFriendlyi=[0]*length
pricei=[0]*length
distancei=[0]*length

for i in range(length):
    idi[i]=(list2[5*i])
    ratingi[i]=(list2[5*i+1])
    veganFriendlyi[i]=(list2[5*i+2])
    pricei[i]=(list2[5*i+3])
    distancei[i]=(list2[5*i+4])

veg=int(input())
maxPri=int(input())
maxDis=int(input())
#print(veg,maxPri,maxDis)

suit=[False]*length

#print(idi,ratingi,veganFriendlyi,pricei,distancei)

finlist=[]
for i in range(length):
    if(veg==1):
        if(veganFriendlyi[i]==veg)and(pricei[i]<=maxPri)and(distancei[i]<=maxDis):
            finlist.append(ratingi[i])
            suit[i]=True
    else:
        if(pricei[i]<=maxPri)and(distancei[i]<=maxDis):
            finlist.append(ratingi[i])
            suit[i]=True
finlist.sort()
finlist.reverse()

#print(finlist)
have=[False]*length
fin=[]
for i in finlist:
    for j in range(length-1,-1,-1):
        if(ratingi[j]==i)and(suit[j])and(not have[j]):
            fin.append(j+1)
            have[j]=True
            break
            
    #fin.append(ratingi.index(i)+1)
    
print(fin)