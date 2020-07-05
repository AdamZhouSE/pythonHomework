short = input()
length = len(short)
k = 1
while k < 30:
    a = input()
    len_of_a = len(a)

    i = 0
    while i + length <= len_of_a:
        if short == a[i:i+length]:
            a = a[0:i] + a[i+length:len(a)]
            len_of_a -= length
            i = -1
        i += 1

    i = 0
    while i < len_of_a:
        if a[i] == " ":
            a = a[0:i] + a[i + 1:len(a)]
            len_of_a -= 1
            i -= 1
        i += 1

    print(a)
    k += 1

