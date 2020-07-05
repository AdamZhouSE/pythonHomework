def afdjk():
    length=int(input())
    aaa=input()
    l=aaa.split(" ")
    l= list(map(int, l))
    l.sort()

    sum=0
    for x in l:
        sum+=x
    if sum%2!=0:
        print('NO')
        return 

    tsum=0
    for x in l:
        tsum+=x
        if tsum=sum/2:
            print('YES')
            return
    
    print('NO')
    return

afdjk()