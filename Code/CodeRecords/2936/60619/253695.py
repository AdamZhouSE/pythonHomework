t = int(input())
phones = []
times = []
for i in range(t):
    oriPhone = list(input().replace("-", ""))
    for j in range(len(oriPhone)):
        if oriPhone[j] == "A" or j == "B" or j == "C":
            oriPhone[j] = "2"
        elif oriPhone[j] == "D" or oriPhone[j] == "E" or oriPhone[j] == "F":
            oriPhone[j] = "3"
        elif oriPhone[j] == "G" or oriPhone[j] == "H" or oriPhone[j] == "I":
            oriPhone[j] = "4"
        elif oriPhone[j] == "J" or oriPhone[j] == "K" or oriPhone[j] == "L":
            oriPhone[j] = "5"
        elif oriPhone[j] == "M" or oriPhone[j] == "N" or oriPhone[j] == "O":
            oriPhone[j] = "6"
        elif oriPhone[j] == "P" or oriPhone[j] == "R" or oriPhone[j] == "S":
            oriPhone[j] = "7"
        elif oriPhone[j] == "T" or oriPhone[j] == "U" or oriPhone[j] == "V":
            oriPhone[j] = "8"
        elif oriPhone[j] == "W" or oriPhone[j] == "X" or oriPhone[j] == "Y":
            oriPhone[j] = "9"
    oriPhone.insert(3, "-")
    phoneNum = ''.join(oriPhone)
    if phoneNum in phones:
        ind = phones.index(phoneNum)
        times[ind] += 1
    else:
        phones.append(phoneNum)
        times.append(1)
for a in range(len(times)):
    if times[a] == 1:
        del(phones[a])
        del(times[a])
        a -= 1
if len(phones) == 0:
    print("No duplicates.")
else:
    k = len(phones)-1
    while k > 0:
        for j in range(k):
            if phones[j] < phones[j+1]:
                temp = phones[j+1]
                phones[j+1] = phones[j]
                phones[j] = temp
                x = times[j+1]
                times[j+1] = times[j]
                times[j] = j
        k -= 1
    for i in range(len(phones)):
        print(phones[i], end=" ")
        print(times[i])