def search(a: int, b: int, k: int) -> int:
    table = []
    for i in range(1, a+1):
        for b in range(1, b+1):
            table.append(i * b)
    table.sort()
    return table[k-1]


a_num = int(input())
b_num = int(input())
k_num = int(input())
print(search(a_num, b_num, k_num))