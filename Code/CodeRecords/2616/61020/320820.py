def possible_or_not(x, y):
    for i in range(y):
        x = x - (i + 1)

    if (x >= 0):
        print("1")
    else:
        print("0")


test_cases = int(input())

for x in range(test_cases):
    input_data = input().split()
    p = input_data[0]
    q = input_data[1]
    possible_or_not(int(p), int(q))

