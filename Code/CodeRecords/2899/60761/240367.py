n=int(input(""))
while(n>1):
    if(n%4==0):
        n/=4
    else:
        print("false")
        break
if n==1:
    print "true"
    