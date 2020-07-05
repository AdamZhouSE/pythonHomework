import math
def main():
    Num=int(input())
    digits=1
    bound=9
    while Num>bound*digits:
        digits+=1
        bound=bound+9*math.pow(10, digits-1)
    start=1
    if digits>1:
        start=int(bound-9*math.pow(10, digits-1)+1)
        distance=0
        if Num-start>=digits:
            distance=(Num-start)%digits
        targetNumber=str(int(math.pow(10,digits-1)+distance))
        result=targetNumber[(Num-start)%digits]
        print(result)
    else:
        print(Num)

if __name__=='__main__':
    main()