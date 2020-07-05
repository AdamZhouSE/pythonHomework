rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def change(x):
    if x <= 26:
        return rows[x - 1]
    else:
        return change(int(x/26))+change(x % 26)


target = int(input())
print(change(target))
