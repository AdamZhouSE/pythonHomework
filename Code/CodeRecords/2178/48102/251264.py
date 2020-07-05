def magic(num: int, ls: list) -> list:
    table = []
    for i in range(1, num+1):
        for j in range(i-1, -1, -1):
            if ls[j:i] not in table:
                table.append(ls[j:i])
        print(len(table))


n = int(input())
lst = input().split(' ')
lst = list(map(int, lst))
magic(n, lst)