n=int(input())
if(n<0):
    print("false")
else:
    while(n%4==0 and n!=1):
        n=n/4
    if(n!=1):
        print('false')
    else:
        print('true')