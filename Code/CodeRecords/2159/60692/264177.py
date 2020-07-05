dict = {1: "I", 4: "IV", 5: "V", 9: "IX",
        10: "X", 40: "XL", 50: "L", 90: "XC",
        100: "C", 400: "CD", 500: "D", 900: "CM",
        1000: "M"}
list1 = list(input())
list1.reverse()
list1 = [int(i) for i in list1]
res = []
for i in range(len(list1) - 1, -1, -1):
    if list1[i] == 9:
        res.append(dict[9 * (10 ** i)])
        list1[i] -= 9
    while 5 <= list1[i] < 9:
        res.append(dict[5 * (10 ** i)])
        list1[i] -= 5
    if list1[i] == 4:
        res.append(dict[4 * (10 ** i)])
        list1[i] -= 4
    while 1 <= list1[i] <= 3:
        res.append(dict[1 * (10 ** i)])
        list1[i] -= 1

print("".join(res))