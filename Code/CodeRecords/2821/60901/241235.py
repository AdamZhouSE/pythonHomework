def question6():
    num = int(input())
    inf = input().split(' ')
    cards = []
    for i in inf:
        cards.append(int(i))
    time = 0
    list = [0,0]
    max = 0
    while not len(cards) == 0:
        if cards[0] > cards[len(cards) - 1]:
            max = cards[0]
            del cards[0]
        else:
            max = cards[len(cards) - 1]
            del cards[len(cards) - 1]
        list[time % 2] += max
        time += 1
    print(list[0],end = ' ')
    print(list[1])

if __name__ == '__main__':
    question6()
