def max_number(boy_num: int, boys: list, girl_num: int, girls: list) -> int:
    boys.sort()
    girls.sort()
    count = 0
    b = g = 0
    while b < boy_num and g < girl_num:
        if abs(boys[b] - girls[g]) <= 1:
            b += 1
            g += 1
            count += 1
        elif boys[b] < girls[g]:
            b += 1
        else:
            g += 1
    return count


boy_n = int(input())
boy = input().split(' ')
boy = list(map(int, boy))
girl_n = int(input())
girl = input().split(' ')
girl = list(map(int, girl))
print(max_number(boy_n, boy, girl_n, girl))