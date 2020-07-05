def print_line(index, n):
    for ii in range(0, (n-index)//2):
        print("*", end="")
    for ii in range(0, index):
        print("D", end="")
    for ii in range(0, (n-index)//2):
        print("*", end="")
    print()


num = int(input())
for i in range(1, num+1, 2):
    print_line(i, num)
for i in range(num-2, -1, -2):
    print_line(i, num)
