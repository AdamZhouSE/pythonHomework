def moon(days: int, size: list):
    len_size = len(size)
    if days == 1:
        if size[len_size-1] == 15:
            return 'DOWN'
        elif size[len_size-1] == 0:
            return 'UP'
        else:
            return -1
    if size[len_size-1] == 15:
        return 'DOWN'
    elif size[len_size-1] == 0:
        return 'UP'
    elif size[len_size-1] > size[len_size-2]:
        return 'UP'
    else:
        return 'DOWN'
    

day = int(input())
size_ls = input().split(' ')
size_ls = list(map(int, size_ls))
print(moon(day, size_ls))