def letters():
    newspaper = input()
    letter = input()
    i = 0
    j = 0
    res = 'YES'
    while i < len(letter):
        if res =='NO':
            break
        if letter[i] == ' ':
            i = i + 1
        while j < len(newspaper):
            if letter[i] == newspaper[j]:
                i = i + 1
                newspaper = newspaper[:j] + newspaper[j + 1:]
                j = 0
                break
            else:
                if j == len(newspaper) - 1:
                    res = 'NO'
                    break
                j = j + 1
        i = i + 1
    print(res,end = '')

letters()
