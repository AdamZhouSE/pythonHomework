def rotate_cards(n):
    deck = [i+1 for i in range(n)]
    res = [0 for i in range(n)]
    for i in range(n):
        deck = deck[(i+1) % len(deck):] + deck[:(i+1) % len(deck)]
        res[deck[0]-1] = i+1
        deck.remove(deck[0])
    return res


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        result.append(rotate_cards(int(input())))
    for i in range(len(result)):
        for j in range(len(result[i])-1):
            print(result[i][j], end=' ')
        print(result[i][len(result[i])-1])