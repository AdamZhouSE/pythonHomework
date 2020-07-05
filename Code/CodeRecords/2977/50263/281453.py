try:
    while True:
        n = input()
        if n == "!":
            break
        result = ""
        for i in range(len(n)):
            m = ord(n[i])
            j = n[i]
            if m in range(65, 91):
                j = chr(155 - m)
            elif m in range(97, 123):
                j = chr(219 - m)
            result+= j
        print(result)
except EOFError:
    pass
        