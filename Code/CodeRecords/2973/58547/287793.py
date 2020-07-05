def func():
    text = input()
    i = int(input())
    lib = {}
    while i > 0:
        lib["".join(sorted(list(input())))] = 0
        i -= 1

    for ele in lib.keys():
        i = 0
        while i < len(text) - len(ele) + 1:
            now = "".join(sorted(list(text[i: i + len(ele)])))
            if now == ele:
                lib[ele] += 1
            i += 1

    print(sum(list(lib.values())))


func()
