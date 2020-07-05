def func():
    num_socks = int(input())
    socks = [int(n) for n in input().split(" ")]

    max_socks = 0
    tables = []
    cursor = 0

    i = 0
    while i < num_socks:
        now_sock = socks[cursor]
        if now_sock not in tables:
            tables.append(now_sock)
        else:
            tables.remove(now_sock)
        if len(tables) > max_socks:
            max_socks = len(tables)
        cursor += 1
        i += 1

    print(max_socks)


func()
