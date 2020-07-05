def duplicate(phone_book):
    std_book = []
    for i in range(len(phone_book)):
        std_book.append(translator((phone_book[i])))
    duplicate_book = []
    while len(std_book) > 0:
        times = std_book.count(std_book[0])
        if times > 1:
            duplicate_book.append((std_book[0], times))
        for i in range(times):
            std_book.remove(std_book[0])
    return duplicate_book


def translator(number):
    std_number = ''
    for i in range(len(number)):
        if number[i] == '-':
            continue
        elif number[i].isalpha():
            if ord(number[i]) < ord('Q'):
                std_number += str(2 + (ord(number[i]) - ord('A')) // 3)
            else:
                std_number += str(2 + (ord(number[i]) - ord('A') - 1) // 3)
        else:
            std_number += number[i]
    return std_number[:3] + '-' + std_number[3:]


raw_book = []
for i in range(int(input())):
    raw_book.append(input())
result = duplicate(raw_book)
if len(result) == 0:
    print('No duplicates.', end='')
else:
    for i in range(len(result)):
        print(result[i][0], result[i][1])