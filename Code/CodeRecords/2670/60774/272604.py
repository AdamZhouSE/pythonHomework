t = int(input())
for i in range(0,t):
    binNum = bin(int(input()))
    com = '0b'
    for j in range(2,len(binNum)):
        com = com + '0' if binNum[j] == '1' else com + '1'
    print(int(com,2))