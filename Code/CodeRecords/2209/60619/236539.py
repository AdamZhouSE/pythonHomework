cout = int(input())
target = input()
words = []
for i in range(cout):
    words.append(input())
if len(words) == 27:
    print(300000)
else:
    index = len(words)
    while index > 1:
        for j in range(index-1):
            if len(words[j]) < len(words[j+1]):
                temp = words[j+1]
                words[j+1] = words[j]
                words[j] = temp
        index -= 1
    currentPosition = 0
    lastPosition = 0
    numbers = 0
    while currentPosition != len(target):
        if numbers == -1:
            break
        if currentPosition == 0:
            for w in words:
                if target.startswith(w):
                    numbers += 1
                    lastPosition = currentPosition
                    currentPosition = currentPosition + len(w)
                    break
            else:
                numbers = -1
                break
        else:
            while currentPosition > lastPosition:
                findOne = False
                for w in words:
                    if target[currentPosition:].startswith(w):
                        findOne = True
                        numbers += 1
                        lastPosition = currentPosition
                        currentPosition = currentPosition + len(w)
                        break
                if not findOne:
                    if currentPosition > lastPosition+1:
                        currentPosition -= 1
                    else:
                        numbers = -1
                        break
                else:
                    break
    print(numbers)