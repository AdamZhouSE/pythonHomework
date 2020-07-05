#讲道理我真不知道这题目在问啥
numOfInput = int(input())
for i in range(numOfInput):
    iN = input().split(" ")
    i = int(iN[0])
    N = int(iN[1])
    print(2**N-i)