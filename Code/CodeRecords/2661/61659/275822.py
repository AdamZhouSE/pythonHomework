T=int(input())

for i in range(0,T):
    num=int(input())
    binary=bin(num)[2:]

    numOfOne=binary.count("1")
    numOfZero=binary.count("0")

    print(numOfOne^numOfZero)