def search1(ls: list) -> int:
    tail = [ls[0]]

    for i in ls[1:]:
        if i > tail[-1]:
            tail.append(i)
            continue
        
        left, right = 0, len(tail)-1
        while left < right:
            mid = (left + right) >> 1
            if tail[mid] >= i:
                right = mid
            else:
                left = mid + 1
        tail[left] = i
    
    return len(tail)


lst = input().split(',')
lst = list(map(int, lst))
print(search1(lst))