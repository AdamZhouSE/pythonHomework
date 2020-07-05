def decompress(letters):
    repeatTimes = int(letters.pop(0))
    nextChar = letters.pop(0)
    string = ""
    while nextChar != "]":
        if nextChar.isdigit():
            repeatTimes = 10*repeatTimes
            repeatTimes = repeatTimes + int(nextChar)
        elif nextChar == "[":
            string = string + decompress(letters)
        else:
            string = string + nextChar
        nextChar = letters.pop(0)
    decompressedString = ""
    for i in range(repeatTimes):
        decompressedString = decompressedString + string
    return decompressedString

letters = input()
letters = list(letters)
letters.append("]")
letters.insert(0,"1")
print(decompress(letters),end = "")