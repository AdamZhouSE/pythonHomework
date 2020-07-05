def amount_of_repeat_num(array):
    array1 = set(array)
    count = 0
    for num in array1:
        if array.count(num) > 1:
            count += 1
    return count


inp = input().split(" ")
n, c, m = int(inp[0]), int(inp[1]), int(inp[2])
colors = [int(x) for x in input().split(" ")]
for i in range(m):
    inp = input().split(" ")
    l, r = int(inp[0]), int(inp[1])
    print(amount_of_repeat_num(colors[l-1:r]))
