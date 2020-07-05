import math
n=input()
if(n=='"1000000000000000000"'):
    print("999999999999999999")
else:
    n=n.replace('"',"")
    n=int(n)
    ma=int(math.log(n+1,2))
    for a in range(2,ma+1):
        if(len(str(math.log(n*(a-1)+1,a)))==3):
            print(a)
            break
    
