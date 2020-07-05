s = input()
print(s[:len(s) // 2] == "".join(reversed(list(s)))[:len(s) // 2])