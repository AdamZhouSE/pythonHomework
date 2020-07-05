M, D = list(map(int, input().split(" ")))
array = []
t = 0
while (M != 0):
    M -= 1
    op = "".join(input().strip().split(" "))
    if (op[0] == 'A'):
        n = eval(op[1:])
        array.append((n + t) % D)
    elif (op[0] == 'Q'):
        L = eval(op[1:])
        nums = array[-L:]
        nums.sort()
        t = nums[-1]
        print(nums[-1])