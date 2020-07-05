if __name__ == '__main__':
    ls1 = input().split(' ')
    ls1 = list(map(int, ls1))
    n, m = ls1[0], ls1[1]
    word = []
    for _ in range(n):
        word.append(input())
    res = []
    for _ in range(m):
        ls2 = input().split(' ')
        ls2 = list(map(int, ls2))
        start = ls2[0] - 1
        end = ls2[1]
        res.append(max(word[start:end]))
    for i in res:
        print(i)
