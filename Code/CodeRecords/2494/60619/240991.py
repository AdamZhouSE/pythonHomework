oriStr = input()
numbers = oriStr[1:len(oriStr)-1].split(",")
pairs = 0
for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if int(numbers[i]) > 2*int(numbers[j]):
            pairs += 1
print(pairs)