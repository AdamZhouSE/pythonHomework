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
    while(i<son):
        if(son%i==0 and mum%i==0):
            son//=i
            mum//=i
        else:
            i+=1
    if(flag==True):
        son = -son
    return str(son)+"/"+str(mum)
LIST = input().split("+")
temp = LIST[0]
for i in range(1,len(LIST)):
    temp = twoNumPlus(temp+"+"+LIST[i])
if(temp[0]==0):
    print("0/1")
else:
    print(temp)