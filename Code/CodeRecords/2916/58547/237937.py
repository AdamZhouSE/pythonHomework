def func():
    n = int(input())
    arr = [int(x) for x in input().split(" ")]

    elements = [4, 8, 15, 16, 23, 42]
    num_of_elements = [0] * 6
    i = 0
    while i < 6:
        num_of_elements[i] = arr.count(elements[i])
        i += 1

    min_num_of_elements = min(num_of_elements)
    min_seq_len = min_num_of_elements * 6
    print(n - min_seq_len)


func()
