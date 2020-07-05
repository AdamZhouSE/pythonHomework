def lst_input(s):
    integers = s[1:-1].split(",")

    b = 0
    while b < len(integers):
        integers[b] = int(integers[b])

        b += 1

    return integers


integers = lst_input(input())
integers.sort()
print(integers)
