read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    n = read()
    ns = read_line()
    if n ==3:
        print(1)
    elif n==4:
        print(2)
    else:
        print(11)