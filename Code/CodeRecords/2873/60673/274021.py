inp = input().split(" ")
allLen = int(inp[0])
numLen = int(inp[1])
numSequence = input().split(" ")
password = input().split(" ")
res = []
for i in range(allLen):
    numSequence[i] = int(numSequence[i])
for i in range(numLen):
    password[i]=int(password[i])
for i in range(allLen):
    if(numSequence[i] in password):
        res.append(numSequence[i])
for i in range(len(res)):
    print(res[i],end="")
    if(i!=numLen-1):
        print(" ",end="")
