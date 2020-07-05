def Ugly(n):
    ptr = 0
    ptr2 = ptr3 = ptr5 = 0
    ugly = [0] * (n + 7)
    ugly[0] = 1

    while ptr < n - 1:
        ugly2 = int(ugly[ptr] / 2) + 1
        ugly3 = int(ugly[ptr] / 3) + 1
        ugly5 = int(ugly[ptr] / 5) + 1

        temporary_ptr = ptr2
        while ugly[temporary_ptr] < ugly2:
            temporary_ptr += 1
        ugly2 = 2 * ugly[temporary_ptr]
        ptr2 = temporary_ptr

        temporary_ptr = ptr3
        while ugly[temporary_ptr] < ugly3:
            temporary_ptr += 1
        ugly3 = 3 * ugly[temporary_ptr]
        ptr3 = temporary_ptr

        temporary_ptr = ptr5
        while ugly[temporary_ptr] < ugly5:
            temporary_ptr += 1
        ugly5 = 5 * ugly[temporary_ptr]
        ptr5 = temporary_ptr

        ptr += 1
        ugly[ptr] = min(ugly2, ugly3, ugly5)

    return ugly[ptr]


number = int(input())
print(Ugly(number))
