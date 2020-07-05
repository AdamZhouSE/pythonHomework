"""
绘制水晶矿
"""


def print_star(num):
    for x in range(0, num):
        print("*", end="")


def print_d(num):
    for x in range(0, num):
        print("D", end="")


n = int(input())
# 从第一行到中间行，D的数量是2*行数-1，*的数量是n -（2*行数-1），D两边各一半
for i in range(1, n+1):
    # 中间行之后与上半部分对称，只要用n-i+1将行数保持一致即可
    if i > n//2+1:
        i = n - i + 1
    num_star = (n - (2*i-1)) // 2
    print_star(num_star)
    print_d(2*i-1)
    print_star(num_star)
    print()

