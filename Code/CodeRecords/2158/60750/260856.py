

def atoi():
    words = input()
    count = 0
    res = ''
    if len(words) == 0:
        print(0)
        return
    for i in range(0,len(words)):
        if words[i] == ' ':
            count += 1
        else:
            if words[i] == '+' or words[i] == '-' or 48 <= ord(words[i]) <= 57:
                res = words[i]
                if i == len(words) - 1:
                    words = ''
                else:
                    words = words[i + 1:]
                break
            else:
                print(0)
                return


    if count == len(words):
        print(0)
        return
    j = 0
    while 48 <= ord(words[j]) <= 57:
        res += words[j]
        j += 1
        if j == len(words):
            break

    if len(res) > 10:
        print(-2147483648)
        return
    if 48 <= ord(res[0]) <= 57 or res[0] == '-':
        print(res)
    else:
        print(res[1:])


atoi()