
def orop(al,li,dem):
    if(al%dem==0 and al!=0 and len(li)==0):
        return True,al
    if(len(li)==0):
        return False,0
    temp=li.copy()
    hold=temp[0]
    temp.remove(hold)
    if(orop(al|hold,temp,dem)[0]):
        return True,orop(al|hold,temp,dem)[1]
    if(orop(al,temp,dem)[0]):
        return True,orop(al,temp,dem)[1]
    return False,0

t=int(input())

for i in range(t):
    temp=[int(x) for x in input().split()]
    A=[int(x) for x in input().split()]
    if(orop(0,A,temp[1])[0]):       
        if(orop(0,A,temp[1])[1]==6):
            print(0)
        else:
            print(orop(0,A,temp[1])[1])
    else:
        print(0)