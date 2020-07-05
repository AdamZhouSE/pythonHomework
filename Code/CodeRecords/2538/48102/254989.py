def find(ls: list) -> int:
    ls.sort()
    while ls[0] <= 0:
        ls.remove(ls[0])
    count = 1
    index = 0
    while index < len(ls) and count == ls[index]:
        index += 1
        count += 1
    return count


lst = eval(input())
print(find(lst))