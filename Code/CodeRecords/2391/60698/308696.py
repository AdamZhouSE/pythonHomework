def test():
    n = int(input())
    names = []
    for _ in range(0, n):
        names.append(input())
    m = int(input())
    already = []
    for _ in range(0, m):
        name = input()
        if name in names:
            if name not in already:
                already.append(name)
                print('OK')
            else:
                print('REPEAT')
        else:
            print('WRONG')


test()
