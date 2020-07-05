def sort4():
    a=input()
    list1 = sorted(a[1:len(a) - 1].split(','),reverse=True)
    number = [int(x) for x in list1]
    res=0
    for i in range(0,len(number)-2):
        for j in range(i+1,len(number)-1):
            for k in range(j+1,len(number)):
                if(number[k]+number[i]>number[j] and number[k]+number[j]>number[i] and number[i]+number[j]>number[k]):
                    if(number[i]+number[j]+number[k]>res):
                        res=number[i]+number[j]+number[k]
    print(res)
    return

sort4()