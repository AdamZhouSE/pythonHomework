def main():
    string=input()
    allLetter=[]
    allNumber=[]
    for i in range(0, len(string)):
        allLetter.append(string[i])
    while "z" in allLetter:
        for letter in "zero":
            allLetter.remove(letter)
        allNumber.append(0)
    while "g" in allLetter:
        for letter in "eight":
            allLetter.remove(letter)
        allNumber.append(8)
    while "x" in allLetter:
        for letter in "six":
            allLetter.remove(letter)
        allNumber.append(6)
    while "w" in allLetter:
        for letter in "two":
            allLetter.remove(letter)
        allNumber.append(2)
    while "h" in allLetter:
        for letter in "three":
            allLetter.remove(letter)
        allNumber.append(3)
    while "s" in allLetter:
        for letter in "seven":
            allLetter.remove(letter)
        allNumber.append(7)
    while "r" in allLetter:
        for letter in "four":
            allLetter.remove(letter)
        allNumber.append(4)
    while "v" in allLetter:
        for letter in "five":
            allLetter.remove(letter)
        allNumber.append(5)
    while "o" in allLetter:
        for letter in "one":
            allLetter.remove(letter)
        allNumber.append(1)
    while "i" in allLetter:
        for letter in "nine":
            allLetter.remove(letter)
        allNumber.append(9)
    allNumber.sort()
    allNumber=list(map(str, allNumber))
    allNumber="".join(allNumber)
    print(allNumber)

if __name__=='__main__':
    main()