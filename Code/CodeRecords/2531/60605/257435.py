
import collections



if __name__ == '__main__':
    t = input().strip()
    t = list(t)
    c = collections.Counter(t)
    c = c.items()
    c = sorted(c, key=lambda vi: vi[1],reverse=True)
    for i in c:
        for j in range(i[1]):
            print(i[0], end="")
    print()