def numop2():
    tb={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    str=input().split('-')
    year=int(str[0])
    month=int(str[1])
    day=int(str[2])
    date=0

    for i in range(1,month):
        if(i==2 and year%4==0):
            date+=29
        else:
            date+=tb.get(i)
    date+=day
    print(date)
    return

numop2()