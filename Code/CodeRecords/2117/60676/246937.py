# 初始时有 n 个灯泡关闭。
# 第 1 轮，你打开所有的灯泡。
# 第 2 轮，每两个灯泡你关闭一次。
# 第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。
# 第 i 轮，每 i 个灯泡切换一次开关。
# 对于第 n 轮，你只切换最后一个灯泡的开关。
# 找出 n 轮后有多少个亮着的灯泡。


def light_bulbs(n):
    count = 0
    for i in range(n):
        if number_of_divisors(i+1) % 2 == 1:
            count += 1
    return count


def number_of_divisors(n):
    if n == 1:
        return 1
    count = 2
    for i in range(1, n//2):
        if n % (i+1) == 0:
            count += 1
    return count


print(light_bulbs(int(input())))