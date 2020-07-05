a = int(input())
for i in range(a):
    aStr = input()
    bStr = input()
    if len(aStr) > len(bStr):
        print("No")
    elif len(aStr) == len(bStr):
        if aStr == bStr:
            print("Yes")
        else:
            print("No")
    else:
        j = 0
        while j < len(bStr):
            if j > len(aStr) - 1:
                if aStr[j - 1] == bStr[j]:
                    print("No")
                    break
                aStr = aStr[0:j] + bStr[j] + aStr[j:]
                j += 1
                continue
            if aStr[j] == bStr[j]:
                j += 1
                continue
            else:
                if aStr[j - 1] == bStr[j]:
                    x = j - 1
                    while aStr[x] == bStr[j] and x >= 0:
                        x -= 1
                    if x < 0:
                        print("No")
                    else:
                        aStr = aStr[0:x + 1] + bStr[j] + aStr[x + 1:]
                    j += 1
                    continue
                else:
                    aStr = aStr[0:j] + bStr[j] + aStr[j:]
                    j += 1
        if aStr == bStr:
            print("Yes")