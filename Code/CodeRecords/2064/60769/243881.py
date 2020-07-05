a = input()
dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
res = 0
jmp = False
for i in range(len(a)):
    if jmp:
        jmp = False
        continue
    if i < len(a) - 1:
        if dict[a[i]] >= dict[a[i + 1]]:
            res += dict[a[i]]
        else:
            res += dict[a[i:i + 2]]
            i += 1
            jmp = True
    else:
        res += dict[a[i]]
print(res)