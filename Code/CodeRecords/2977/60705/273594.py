strings = []
l = input()
while l != "!":
    strings.append(list(l))
    l = input()
    
for x in strings:
    for i in range(0, len(x)):
        if ord("a") <= ord(x[i]) <= ord("z"):
            x[i] = chr(219-ord(x[i]))
        elif ord("A") <= ord(x[i]) <= ord("Z"):
            x[i] = chr(155-ord(x[i]))
        else:
            x[i] = x[i]
    b = ""
    for i in range(0, len(x)):
        b += x[i]
    print(b)