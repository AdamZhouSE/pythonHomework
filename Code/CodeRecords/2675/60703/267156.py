T = int(input())
for m in range(T):
    numList = list(input())
    initial = int("".join(numList))
    for i in range(len(numList)):
        if numList[i]=='6':
            numList[i]='9'
    after = int("".join(numList))
    print(after-initial)