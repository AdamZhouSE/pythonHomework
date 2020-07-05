def palin(s):
    x = list(s)
    times = int((len(x)+1) / 2)
    for i in range(times):
        if x[i] != x[len(x)-1-i]:
            return False
    return True


if __name__ == "__main__":
    s = input()
    print(palin(s))
