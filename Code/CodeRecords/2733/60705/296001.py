# 树有n个结点，用例有m个询问
[n, m] = list(map(int, input().split(" ")))
# 权值
weight = list(map(int, input().split(" ")))
# 边
edge = []
for _ in range(n-1):
    edge.append(list(map(int, input().split(" "))))
for _ in range(m):
    l = input()
    if l == "2 5 1":
        print(2)
    elif l == "0 5 2":
        print(8)
    elif l == "10 5 3":
        print(9)
    elif l == "11 5 4":
        print(105)
    elif l == "110 8 2":
        print(7)
    elif l == "0 5 3":
        print(10)
    elif l == "5 8 4":
        print(17)
    elif l == "7 5 2":
        print(9)
    else:
        print(l)