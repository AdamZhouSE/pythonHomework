wordList = input()
a = []
b = ''
i = 0
while i < len(wordList):
    if wordList[i]>='0' and wordList[i]<='9' :
        b += wordList[i]
        j = i+1
        while wordList[j]>='0' and wordList[j]<='9':
            b += wordList[j]
            j += 1
            i += 1
        a.append(b)
        b = ''
    i += 1;

number = []
for i in range(0,len(a)):
    number.append(int(a[i]))

if len(number)==1:
    print(0)
else:
    for i in range(0,len(number)-1):
        for j in range(0,len(number)-1):
            if number[j] > number[j+1]:
                number[j+1] = number[j] + number[j+1]
                number[j] = number[j+1] - number[j]
                number[j+1] = number[j+1] - number[j]

    max = number[1] - number[0]
    for i in range(0,len(number)-1):
        if number[i+1] - number[i] > min:
            max = number[i+1] - number[i]
    print(max)
