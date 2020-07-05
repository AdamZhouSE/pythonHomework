def test():
    s = input()
    table = []
    count = 0
    for c in s:
        if c in table:
            count += 1
        else:
            table.append(c)
    print(count)

for i in range(int(input())):
    test()