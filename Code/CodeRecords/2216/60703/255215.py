import re
def twoNumPlus(STR:str):
    numlist = [int(x) for x in re.split("\+|/",STR)]
    son1 = numlist[0]
    son2 = numlist[2]
    mum1 = numlist[1]
    mum2 = numlist[3]
    mum = mum1*mum2
    son1 = mum2*son1
    son2 =mum1*son2
    son = son1+son2
    if(son<0):
        flag = True
    else:
        flag = False
    son = abs(son)
    i = 2
    while(i<=son and son!=1):
        if(son%i==0 and mum%i==0):
            son//=i
            mum//=i
        else:
            i+=1
    if(flag==True):
        son = -son
    return str(son)+"/"+str(mum)
LIST =[]


LIST1 = input().split("+")
for i in LIST1:
    if("-" in i and i[0]!='-'):
        temp1  = i.split("-")
        for j in range(0,len(temp1)):
            if j==0:
                LIST.append(temp1[j])
            else:
                LIST.append("-"+temp1[1])

    else:
        LIST.append(i)
temp = LIST[0]
for i in range(1,len(LIST)):
    temp = twoNumPlus(temp+"+"+LIST[i])
if(temp[0]=='0'):
    print("0/1")
else:
    print(temp)