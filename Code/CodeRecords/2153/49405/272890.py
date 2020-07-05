s = input()
if s[0] == "-": print("-" + str(int("".join(reversed(list(s[1:]))))))
else: print(int("".join(reversed(list(s)))))