s1, s2 = sorted(input()), input()
for i in range(len(s2) - len(s1) + 1):
    if sorted(s2[i: i + 2]) == s1:
        print(True)
        break
else:
    print(False)
