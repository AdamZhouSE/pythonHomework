t = int(input())
for i in range(0,t):
    binNum = bin(int(input()))[2:]
    binNum = binNum.zfill(32)
    com = '0b'
    for j in range(0,len(binNum)):
        com = com + '0' if binNum[j] == '1' else com + '1'
    print(int(com,2))