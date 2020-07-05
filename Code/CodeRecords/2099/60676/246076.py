def transformer(string):
    res = 0
    for i in range(len(string)):
        res = 26 * res + ord(string[i]) - ord('A') + 1
    return res


print(transformer(input()))