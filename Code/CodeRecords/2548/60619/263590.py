t = int(input())
for ind in range(t):
    string = input()
    k = int(input())
    maxL = 0
    for i in range(len(string)):
        chara = []
        length = 0
        for j in range(i, len(string)):
            if string[j] in chara:
                length += 1
            else:
                if len(chara) <= k-1:
                    chara.append(string[j])
                    length += 1
                else:
                    break
        if length > maxL:
            maxL = length
    print(maxL)