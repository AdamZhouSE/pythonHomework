handshakes = [1,1,2,5,14]
for i in range(26):
    length = len(handshakes)
    mysum = 0
    for i in range(length):
        mysum += handshakes[i] * handshakes[length-1-i]

    handshakes.append(mysum)

#print(handshakes)
testCases = int(input().strip())
while testCases > 0:
    testCases -= 1
    n = int(input().strip()) // 2
    print(handshakes[n])