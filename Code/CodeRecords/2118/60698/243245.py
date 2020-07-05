import math

def test():
    a = int(input())
    if(a<=0):
        print(False)
        return
    b = math.log(a,3)
    print(b % 1==0)
    
test()
