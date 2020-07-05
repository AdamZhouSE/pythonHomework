t=int(input())
for i in range(t):
    num=int(input())
    b=list(bin(num)[2:])
    numOfZero=b.count('0')
    numOfOne=b.count('1')
    res=numOfOne^numOfZero
    print(res)