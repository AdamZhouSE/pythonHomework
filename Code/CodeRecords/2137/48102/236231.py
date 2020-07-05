def perfect():
    num = int(input())
    if num == 1:
        return False
    sqrt_num = int(num ** 0.5)
    ls = [1]
    for i in range(2, sqrt_num, 1):
        if num % i == 0:
            ls.append(i)
            ls.append(num // i)
    return sum(ls) == num


print(perfect())