if __name__ == '__main__':
    n = eval(input())
    players = input().split()
    for i in range(n):
        players[i] = int(players[i])
    res = n
    circles = []
    for i in players:
        if i not in circles:
            length = 1
            next = players[i - 1]
            circles.append(i)
            while next not in circles:
                circles.append(next)
                length += 1
                next = players[next - 1]
            if 1 < length < res:
                res = length
    print(res, end='')