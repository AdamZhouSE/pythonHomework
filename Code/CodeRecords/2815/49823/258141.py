def l(n,l):
    numOfZero = sum([1 if i == 0 else 0 for i in l])
    step=sum([min(abs(i-1),abs(i+1)) if i!=0 else 0 for i in l])+numOfZero
    numOfMinusOne=sum([0 if abs(i-1)<=abs(i+1) else 1 for i in l])
    print(step if numOfMinusOne%2==0 else step+2)
if __name__ == '__main__':
    l(int(input()), [int(i) for i in input().split(' ')])
