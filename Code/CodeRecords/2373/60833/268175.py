lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))
for i in range(0,n):
    count=int(lines.pop(0))
    list_number = list(lines.pop(0).split(" "))
    list_number = list(map(int, list_number))
    if(count<=0):
        print(0)
    elif(count==1):
        print(list_number[0])
    else:
        excl=0
        incl=list_number[0]
        excl_new=0
        for i in range(1,count):
            if excl>incl:
                excl_new=excl
            else:
                excl_new=incl
            incl=excl+list_number[i]
            excl=excl_new
        if excl>incl:
            print(excl)
        else:
            print(incl)