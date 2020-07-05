while True:
    try:
        source = input()
        if source=="0 0":
            break
        nm = source.split(' ')
        m = int(nm[0])
        n = int(nm[1])
        result = []
        if m <= n:
            result.append(m)
        ptr = 0
        while ptr < len(result):
            m = result[ptr]
            if 2 * m <= n:
                result.append(2 * m)
            if 2 * m + 1 <= n:
                result.append(2 * m + 1)
            ptr += 1
        print(len(result))
    except EOFError:
        break
    