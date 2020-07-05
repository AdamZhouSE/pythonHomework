def equal(str1, str2):
    l1 = list(str1)
    l2 = list(str2)
    for item in l1:
        if item in l2:
            l2.remove(item)
        else:
            return False
    return True


num = int(input())
for i in range(num):
    str1 = input()
    str2 = input()
    res = 0
    for j in range(len(str1) - len(str2) + 1):
        if equal(str1[j:j + len(str2)], str2):
            res += 1
    print(res)
