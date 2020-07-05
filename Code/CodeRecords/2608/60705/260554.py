def f(s:str) -> list:
    l = []
    for i in range(1, len(s)-1):
        l.append(s[:i] + s[i+1:])
    for i in range(0, len(l)):
        if len(l[i]) > 2:
            new_a = f(l[i])
            for j in new_a:
                l.append(j)
    return l


if __name__ == '__main__':
    n = int(input())
    yuanyin = ['a', 'e', 'i', 'o', 'u']
    for test in range(0, n):
        l = []
        s = input()
        for i in range(0, len(s)):
            if s[i] in yuanyin:
                for j in range(i+1, len(s)):
                    if s[j] not in yuanyin:
                        l.append(s[i:j+1])
        for i in range(0, len(l)):
            if len(l[i]) > 2:
                new_a = f(l[i])
                for j in new_a:
                    l.append(j)
        l = list(set(l))
        l.sort()
        if len(l) == 0:
            print(-1)
        else:
            print(l[0], end="")
            for items in range(1, len(l)):
                print(" "+l[items], end="")
        print()

