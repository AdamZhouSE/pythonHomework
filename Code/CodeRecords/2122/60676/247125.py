# 有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
# 如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
# 你允许：
# 装满任意一个水壶
# 清空任意一个水壶
# 从一个水壶向另外一个水壶倒水，直到装满或者倒空


def pour_water(x, y, z):
    if z > max(x, y):
        return False
    if z % min(x, y) in possible_divisors(x, y):
        return True
    return False


def possible_divisors(x, y):
    gcd = 1
    for i in range(min(x, y), 1, -1):
        if x % i == 0 and y % i == 0:
           gcd = i
           break
    divisors = [0, gcd]
    while divisors[-1] + gcd < min(x, y):
        divisors.append(divisors[-1] + gcd)
    return divisors


print(pour_water(int(input()), int(input()), int(input())))