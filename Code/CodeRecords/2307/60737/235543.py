def maj_element(x, s):
    n = x / 2
    rank = get_rank(s)
    maj = [0] * len(rank)
    for i in range(0, len(s)):
        for j in range(0, len(rank)):
            if s[i] == rank[j]:
                maj[j] += 1
    for i in range(0, len(maj)):
        if maj[i] >= n:
            return rank[i]
    return -1


def get_rank(s):
    rank = []
    rank.append(s[0])
    for i in range(1, len(s)):
        for j in range(0, len(rank)):
            if s[i] == rank[j]:
                break
        rank.append(s[i])
    return rank


if __name__ == "__main__":
    turn = int(input())
    while turn > 0:
        x = int(input())
        s = input().split( )
        print(maj_element(x, s))
        turn -= 1
