def gap(i):
    sign = 0
    while(i>0):
        if(i%2==1):
            sign=sign+1
        else:
            sign=0
        if(sign==2):
            return False
        i=int(i/2)
    return True

def discontinuous():
    num = int(input())
    out = 0
    for i in range(num+1):
        if(gap(i)):
            out = out+1
    print(out)