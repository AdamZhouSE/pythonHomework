n=int(input())
if(n==0):
    print('0')
else:
    res=""
    while (n != 0) :
        if(n%2==0):
            res="0"+res
            n=int(n/(-2))
        else:
            res="1"+res
            n=int((n-1)/(-2))
    print(res)