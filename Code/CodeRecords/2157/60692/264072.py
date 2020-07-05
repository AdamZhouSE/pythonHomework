list1 = list(input())
dict = {"I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000}
i = 0
res = 0
while i < len(list1):
    if i < len(list1) - 1:
        if dict[list1[i]] < dict[list1[i + 1]]:
            res += (dict[list1[i + 1]] - dict[list1[i]])
            i += 2
        else:
            res += dict[list1[i]]
            i += 1
    else:
        res += dict[list1[i]]
        i += 1
print(res)