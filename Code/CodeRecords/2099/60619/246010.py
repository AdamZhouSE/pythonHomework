rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def change(x):
    return rows.index(x)+1


target = input()
length = len(target)
result = 0
for i in range(length):
    result += change(target[length-1-i]) * (26**i)
print(result)