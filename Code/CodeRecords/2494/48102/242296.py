def double(ls: list) -> int:
    count = 0
    for i in range(len(ls)-1):
        for j in ls[i+1:]:
            if ls[i] > 2 * j:
                count += 1
    return count


lst = eval(input())
print(double(lst))