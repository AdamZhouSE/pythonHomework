def bags(index: int, capacity: int):
    if index > total_toy_num - 1 or capacity <= 0:
        return 0
    return max(bags(index + 1, capacity), bags(index + 1, capacity - toys[index]) + 1)

for _ in range(eval(input())):
    total_toy_num, total_capacity = list(map(int, input().split(' ')))
    toys = list(map(int, input().split(' ')))
    print(bags(0, total_capacity))
