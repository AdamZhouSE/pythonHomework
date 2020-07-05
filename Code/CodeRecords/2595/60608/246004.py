import re
def func2():
    num = int(input())
    array1 = []
    while num > 0:
        num -= 1
        tem = 1
        array2 = list(map(int, re.findall(r'\d+', input())))
        while array2[0] > 1:
            tem *= array2[1]
            array2[0] -= 1
        array1.append(tem)
    for item in array1:
        print(item)
func2()