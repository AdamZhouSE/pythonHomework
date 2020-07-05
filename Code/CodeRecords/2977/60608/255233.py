def func11():
    t = input()
    while t != "!":
        res = []
        for char in list(t):
            if char.isalpha():
                if char.islower():
                    res.append(chr(-ord(char)+ord("a")+ord("z")))
                else:
                    res.append(chr(-ord(char)+ord("A")+ord("Z")))
            else:
                res.append(char)
        print("".join(res))
        t = input()


func11()