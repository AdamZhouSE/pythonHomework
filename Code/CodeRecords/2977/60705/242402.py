def qufan(s):
    if ord("a") <= ord(s) <= ord("z"):
        return chr(219-ord(s))
    elif ord("A") <= ord(s) <= ord("Z"):
        return chr(155-ord(s))
    else:
        return s


if __name__ == "__main__":
    while True:
        a = input()
        if a == "!":
            break
        b = ""
        for i in range(0, len(a)):
            b += qufan(a[i])
        print(b)
