s = list(input())
for c in s:
    if not (c.isdigit() or c == "e" or c == "."):
        print(False)
        exit()
print(True)