maxcomein=0

def digui(list,maxtime,now,shouru):
    global maxcomein
    if now>maxtime:
        if shouru>maxcomein:
            maxcomein=shouru
    else:
        for i in range(0,len(list)):
            if list[i][0]>=now:
                digui(list,maxtime,list[i][1],shouru+list[i][2])



if __name__ == "__main__":
    a=input()
    a=a.replace("[","")
    a=a.replace("]","")
    b=a.split(',')
    for i in range(0,len(b)):
        b[i]=int(b[i])
    qishi=b
    a = input()
    a = a.replace("[", "")
    a = a.replace("]", "")
    b = a.split(',')
    for i in range(0, len(b)):
        b[i] = int(b[i])
    zhongzhi=b
    a = input()
    a = a.replace("[", "")
    a = a.replace("]", "")
    b = a.split(',')
    for i in range(0, len(b)):
        b[i] = int(b[i])
    shouru=b
    maxtime=max(qishi)
    list=[]
    for i in range(0,len(qishi)):
        temp=[]
        temp.append(qishi[i])
        temp.append(zhongzhi[i])
        temp.append(shouru[i])
        list.append(temp)
    digui(list,maxtime,0,0)
    print(maxcomein)
