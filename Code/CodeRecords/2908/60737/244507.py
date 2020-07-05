def clasify(alph):
    beta = []
    for i in range(len(alph)):
        alph[i].sort()
        beta.append(''.join(alph[i]))
    beta = list(set(beta))
    return len(beta)


if __name__ == "__main__":
    n = int(input())
    alph = []
    while n:
        alph.append(list(input()))
        n -= 1
    print(clasify(alph), end="")
