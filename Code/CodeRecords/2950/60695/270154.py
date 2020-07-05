string = input()
if string[len(string)-1] == "2":
    print("-1")
elif string.replace("25", "") == "":
    print(1)
else:
    c2 = 0
    c5 = 0
    for i in range(0, len(string)):
        if string[i] == "2":
            c2 += 1
        else:
            c5 += 1
    if c2 == c5:
        print(2)
    else:
        print("-1")