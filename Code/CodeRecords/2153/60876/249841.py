string=input()
if string.startswith("-"):
    print("-",end="")
    print((string[::-1])[0:len(string)-1])
else:
    if string.endswith("0"):
        print((string[::-1])[1:len(string)])
    else:
        print(string[::-1])