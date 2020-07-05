def min_move():
    ls = input().split(',')
    ls = list(map(int, ls))
    min_value = min(ls)
    count = 0
    for i in ls:
        count += i - min_value
    return count


print(min_move())