def containsYes(string, characters):
    for i in characters:
        gotIt = False
        for j in string:
            if i == j:
                gotIt = True
                break
        if not gotIt:
            return False
    return True



def judge():

        string = input()

        #     count numbers of character types
        stringCount = list(string)
        stringCount.sort()
        tempCMP = stringCount[0]
        characters = [tempCMP]
        for i in range(0, len(stringCount)):
            if tempCMP != stringCount[i]:
                tempCMP = stringCount[i]
                characters.append(tempCMP)
        #     mission completed
        length = len(characters)
        for i in range(length, len(string)):
            for j in range(0, len(string) - i + 1):
                stringGot = string[j: j + i ]
                if containsYes(stringGot, characters):
                    print(i)
                    return


n = int(input())
for i in range(0, n):
    judge()