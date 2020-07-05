def func26():
    n = input()
    while n[-1] == "0":
        n = n[:-1]
    if n[0] == "-":
        n = n[1:]
        print("-"+n[::-1])
    else:
        print(n[::-1])
    return
func26()