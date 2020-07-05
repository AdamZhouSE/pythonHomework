def isContradict(str1, str2):
    cont = False
    for ch1 in str1:
        for ch2 in str2:
            if ch1 == ch2:
                cont = True
    return cont

str = input()[1:-1].split(",")
str = [x[1:-1] for x in str]
length = [len(x) for x in str]
maxMul = 0
for i in range(len(str)):
    for j in range(i+1, len(str)):
        if not isContradict(str[i], str[j]):
            temp = len(str[i])*len(str[j])
            if temp > maxMul:
                maxMul = temp
print(maxMul)
