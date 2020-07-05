s = input() + " "
ans = 0
m = {"V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
for i in range(len(s) - 1):
    if s[i] == "I":
        if s[i + 1] == "V" or s[i + 1] == "X":
            ans -= 1
        elif s[i + 1] == "L" or s[i + 1] == "C":
            ans -= 10
        elif s[i + 1] == "D" or s[i + 1] == "M":
            ans -= 100
        else: ans += 1
    else: ans += m[s[i]]
print(ans)