def int_list(int1):
    str1 = str(int1)
    list1 = list(str1)
    return list1
a = int(input())
j = a
while (j >= a):
    for i in range(2, j):
        if j % i == 0:
            break
    else:
        lisj = int_list(j)
        if lisj[::-1] == lisj:
            print(j)
            break
    j = j + 1