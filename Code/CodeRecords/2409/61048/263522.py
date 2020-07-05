def numop3():
    chips=input().split(',')
    array = [int(x) for x in chips]
    count = 0
    for number in array:
        number=number%2
        if(number==1):
            count+=1
    numOf1=count
    numOf0=len(chips)-count
    if(numOf1>=numOf0):
        res=numOf0
    else:
        res=numOf1
    print(res)
    return

numop3()