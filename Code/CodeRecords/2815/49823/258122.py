def l(n,l):
    step=sum([min(abs(i-1),abs(i+1)) for i in l])
    numOfMinusOne=sum([0 if abs(i-1)<abs(i+1) else 1 for i in l])
    #noZero=not 0 in l
    print(step if numOfMinusOne%2==0 and noZero else step+2)
if __name__ == '__main__':
    l(int(input()), [int(i) for i in input().split(' ')])
