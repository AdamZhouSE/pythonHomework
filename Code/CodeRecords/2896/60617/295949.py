def Anonymous():
    paper=input().split(" ")
    Anonymous_le=input().split(" ")
    allLetters=[]
    for words in paper:
        for letter in words:
            allLetters.append(letter)
    while True:
        for words in Anonymous_le:
            for letter in words:
                if letter not in allLetters:
                    print("NO")
                    exit()
                else:
                    allLetters.remove(letter)
        print("YES")
        exit()

if __name__=='__main__':
    Anonymous()
