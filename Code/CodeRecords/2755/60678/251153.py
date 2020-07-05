times = int(input())
for loopTimes in range(0, times):
    arrayA = input().split()
    arrayB = input().split()
    outcomeExp = len(arrayA) + len(arrayB) - 2
    arrayOutcome = []
    for i in range(0, outcomeExp + 1):
        arrayOutcome.append(0)
    for i in range(0, len(arrayA)):
        for j in range(0, len(arrayB)):
            exp = i + j
            sig = int(arrayA[i]) * int(arrayB[j])
            arrayOutcome[exp] += sig

    for i in range(0, len(arrayOutcome)):
        arrayOutcome[i] = str(arrayOutcome[i])
    print(' '.join(arrayOutcome))