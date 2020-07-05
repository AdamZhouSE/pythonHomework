import math
n = int(input())
s = ''
if(n==0):
    print("0")
else:
    
    while(n!=0):
        s += str(n%2)
        n = math.ceil((n/(-2)))
        print(n)
    print(s[::-1])