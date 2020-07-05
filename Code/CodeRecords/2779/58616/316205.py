tcs = int(input())
while tcs > 0:
    tcs-=1
    num=int(input(""))
    list1=list(map(int,input("").split()))
    mini=min(list1)
    maxi=max(list1)
    i=mini
    cf=1
    while(i>=1) :
        if maxi % i ==0 and mini % i ==0 :
            cf=i
            break
        i-=1
    ans= mini * maxi /cf
    print(int(ans))