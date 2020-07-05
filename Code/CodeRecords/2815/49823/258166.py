def l(n,l):
    existZero=0 in l
    step=sum([min(abs(i-1),abs(i+1)) for i in l])
    numOfMinusOne = sum([0 if abs(i - 1) <= abs(i + 1) else 1 for i in l])
    print(step if numOfMinusOne % 2 == 0 or (numOfMinusOne % 2 == 1 and existZero) else step + 2)
if __name__ == '__main__':
    l(int(input()), [int(i) for i in input().split(' ')])
