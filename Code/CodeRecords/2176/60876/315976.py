string=input()
temp=list(string)
temp.reverse()
newone=sorted(string)
if len(string)<20:
    for i in range(0,len(temp)):
        item=newone[i]
        index=temp.index(item)
        temp[index]=","
        if i!=len(temp)-1:
            print(len(temp)-index,end=" ")
        else:
            print(len(temp)-index)