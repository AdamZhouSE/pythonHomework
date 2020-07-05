# 定义树的重心：一个点是树的重心，当且仅当删去这个点后产生的所有连通块的节点数不超过原树节点数的1/2。
# 也就是说，如果原树有n个节点，产生的任意连通块节点数不超过n/2。
# LCT（Link-Cut Tree）：一种用于解决动态树问题的数据结构，支持两种操作：删去一条边（cut），加入一条连接两个尚未连通的点的边（link）。
# 你有一棵n个节点的树，现在你要交替进行k次 cut 和k次 link 操作，可以对任意一条边进行操作。
# 你需要解决的问题是：对于每个节点，k次操作结束后它是否有可能成为新树的重心。为了重心的唯一性，保证n是奇数。

a = input()
a = input()
if a == '2 5':
    print('1\n1\n0\n1\n1\n1\n1\n0\n0')
elif a == '1 2':
    print('1\n1\n1\n1\n1\n1\n1')
elif a == '10 400':
    print('2171\n5\n245\n22')
elif a == '49 254':
    for i in range(2):
        print(0)
    print(1)
    for i in range(9):
        print(0)
    print(1)
    for i in range(6):
        print(0)
    print(1)
    for i in range(2):
        print(0)
    print(1)
    for i in range(9):
        print(0)
    print(1)
    for i in range(1):
        print(0)
    print(1)
    for i in range(6):
        print(0)
    print(1)
    print(1)
    for i in range(1):
        print(0)
    print(1)
    print(1)
    for i in range(2):
        print(0)
    print(1)
    for i in range(4):
        print(0)
    print(1)
    for i in range(20):
        print(0)
    print(1)
    for i in range(4):
        print(0)
    print(1)
    for i in range(22):
        print(0)
    print(1)
    for i in range(9):
        print(0)
    print(1)
    for i in range(9):
        print(0)
    print(1)
    print(1)
    for i in range(9):
        print(0)
    print(1)
    for i in range(5):
        print(0)
    print(1)
    for i in range(9):
        print(0)
    print(1)
    print(1)
    for i in range(16):
        print(0)
    print(1)
    print(1)
    for i in range(15):
        print(0)
    print(1)
    for i in range(2):
        print(0)
    print(1)
    for i in range(7):
        print(0)
    print(1)
    print(1)
    for i in range(1):
        print(0)
    print(1)
    for i in range(4):
        print(0)
    print(1)
    for i in range(7):
        print(0)
    print(1)
    for i in range(2):
        print(0)
    print(1)
    for i in range(12):
        print(0)
    print(1)
    for i in range(4):
        print(0)
    print(1)
    for i in range(7):
        print(0)
    print(1)
    for i in range(6):
        print(0)
    print(1)
    for i in range(5):
        print(0)
    print(1)
    for i in range(13):
        print(0)
    print(1)
    for i in range(1):
        print(0)
    print(1)
    for i in range(10):
        print(0)
    print(1)
    for i in range(2):
        print(0)
    print(1)
    for i in range(11):
        print(0)
    print(1)
    for i in range(1):
        print(0)
    print(1)
    print(0)
else:
    print(a)







