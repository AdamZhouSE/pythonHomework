x=int(input())
y=int(input())
tar=int(y/2)
iseven=0
if y%2==0:iseven=1  # y is even
if x>=y:
    print(x-y)
else:
    optimes=0
    while x<tar:
        x*=2
        optimes+=1
    # x is between y/2 and y
    dis1=x-tar
    dis2=2*x-y
    if dis1<=dis2:
        if iseven:
            optimes+=x-tar+1  # x only need to decrease to y/2 and then double
        else:
            optimes+=x-tar-1+1+1  # first 1 to get the number 1 bigger han tar,second 1 is to double,third 1 is to decrese
    else:
        optimes=1+2*x-y
    print(optimes)