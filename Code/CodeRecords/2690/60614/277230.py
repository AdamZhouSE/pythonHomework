def check(remainingStr,remainingKey):
    if len(remainingKey)==0:
        return 1
    else:
        keyNow=remainingKey[0]
        count=0
        for i in range(len(remainingStr)):
            if remainingStr[i]==keyNow:
                count+=check(remainingStr[i:],remainingKey[1:])
        return count
length=int(input())
for i in range(length):
    input()
    init=input().split()
    str=init[0]
    key=init[1]
    print(check(str,key))