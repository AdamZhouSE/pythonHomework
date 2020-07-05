"""
题目描述
    有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
    如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
    你允许：
        装满任意一个水壶
        清空任意一个水壶
        从一个水壶向另外一个水壶倒水，直到装满或者倒空
"""


def canMeasureWater(x: int, y: int, z: int) -> bool:
    def gcd(a: int, b: int) -> int:
        if b == 0:
            return a
        return gcd(b, a % b)

    return z == 0 or (z <= x + y and z % gcd(x, y) == 0)


print(canMeasureWater(int(input()), int(input()), int(input())))
