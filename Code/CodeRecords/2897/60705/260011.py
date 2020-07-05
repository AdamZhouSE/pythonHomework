def con(a, b):
    for i in b:
        if i in a:
            return True
    return False


if __name__ == '__main__':
    words = input()[1:-1].split(",")
    for i in range(0, len(words)):
        words[i] = words[i][1:-1]
    m = 0
    for i in range(0, len(words)):
        for j in range(i+1, len(words)):
            if con(words[i], words[j]):
                continue
            if len(words[i]) * len(words[j]) > m:
                m = len(words[i]) * len(words[j])
    print(m)