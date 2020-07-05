def main():
    begin_word = input()
    end_word = input()
    words = eval(input())
    paths = [[begin_word]]
    result = []
    while True:
        n = len(paths)
        for i in range(0, n):
            past = paths[i][len(paths[i]) - 1]
            for j in range(0, len(words)):
                if words[j] not in paths[i] and one_letter_difference(past, words[j]):
                    if words[j] == end_word:
                        result.append(paths[i] + [end_word])
                    else:
                        paths.append(paths[i] + [words[j]])
        if n == len(paths):
            break
        else:
            paths = paths[n:]
    result = sorted(result,key=lambda x:len(x))
    length = 0
    for i in range(0, len(result)):
        if i == 0:
            length = len(result[i])
        else:
            if len(result[i]) > length:
                result = result[:i]
                break
    print(result)


def one_letter_difference(word, standard):
    result = False
    for i in range(0, len(word)):
        if word[i] != standard[i]:
            if result:
                result = False
                break
            else:
                result = True
    return result


if __name__ == '__main__':
    main()
