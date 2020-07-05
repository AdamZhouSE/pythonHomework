str = input()

i = 0
lst = []
while i < len(str):
    number = ''
    judge = False
    if str[i]=='-' or (str[i]>='0' and str[i]<='9'):
        judge = True
        number += str[i]
    while judge:
        if i + 1 == len(str):
            lst.append(int(number))
            break
        if str[i + 1] >= '0' and str[i + 1] <= '9':
            i += 1
            number += str[i]
        else:
            judge = False
            lst.append(int(number))
    i += 1

if len(lst) == 0:
    print("0")
else:
    words = []
    words.append(lst[0])
    max = 1
    number = 0
    for i in range(1,len(lst)):
        if lst[i] <= words[len(words)-1]:
            j = 0
            lens = len(words)
            while j < len(words)-1:
                if lst[i] < words[len(words)-1-j]:
                    words[len(words)-1-j] = lst[i]
                    words = words[0:len(words)-j]
                    if len(words)<lens:
                        j += 1
                else:
                    break
        else:
            words.append(lst[i])
            number = len(words)
            if max < number:
                max = number
    print(max)

