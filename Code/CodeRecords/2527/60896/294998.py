def takeSecond(elem):
    return elem[1]

list1=eval(input())
veg=eval(input())
maxprice=eval(input())
maxdist=eval(input())
result=[]
for i in range(0,len(list1)):
    if(veg==1):
        if(list1[i][2]==1):
            if(list1[i][3]<=maxprice):
                if(list1[i][4]<=maxdist):
                    result.append(list1[i])
    else:
        if(list1[i][3]<=maxprice):
            if(list1[i][4]<=maxdist):
                result.append(list1[i])
result.sort(reverse=True)
result.sort(key=takeSecond,reverse=True)
result2=[]
for i in range(0,len(result)):
    result2.append(result[i][0])
else:
    print(result2)
