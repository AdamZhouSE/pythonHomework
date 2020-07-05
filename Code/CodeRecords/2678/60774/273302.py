t = int(input())
for i in range(0,t):
    binNum = bin(int(input()))
    if(binNum.count('1') != 1):
        print(-1)
    else:
        print(binNum.index('1'))