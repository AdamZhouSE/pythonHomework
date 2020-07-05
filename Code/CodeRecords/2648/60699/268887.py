prev = input()
str = str(prev)
toBedeleted = input()
if len(toBedeleted) == 0:
    print(prev, end="")
else:
    while toBedeleted in prev:
        k = prev.index(toBedeleted)
        prev = prev[0:k] + prev[k + len(toBedeleted):]
        if prev == toBedeleted:
            break

    print(prev, end="")