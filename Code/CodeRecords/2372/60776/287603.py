a=int(input())
for i in range(0,a):
    str=input()
    newstr=str.split(' ')
    n=int(newstr[0])
    x=int(newstr[1])
    y=int(newstr[2])
    temp = input()
    newx = temp.split(' ')
    for j in range(0,len(newx)):
        if newx[j]=='':
            del newx[j]

    for j in range(0, len(newx)):
        newx[j] = int(newx[j])
    temp = input()
    newy = temp.split(' ')
    for j in range(0,len(newx)):
        if newy[j]=='':
            del newy[j]
    for j in range(0, len(newy)):
        newy[j] = int(newy[j])
    countx=[]
    county=[]
    tongyang=[]
    result=0
    for j in range(0,len(newx)):
        if(newx[j]>newy[j]):
            countx.append(newx[j])
        elif(newx[j]<newy[j]):
            county.append(newy[j])
        else:
            tongyang.append(newx[j])
    result=sum(countx)+sum(county)+sum(tongyang)
    print(result)