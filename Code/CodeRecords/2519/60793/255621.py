def is_triangle(ls:list) -> list:
    ls = list(map(int, ls))
    if len(ls) < 3:
        return [0]
    else:
        ls = list(sorted(ls))
        a, b, c = ls[-3], ls[-2], ls[-1]
        if a + b > c:
            return [a, b, c]
        else:
            return is_triangle(ls[:-1])


the_ls = list(map(int, input()[1:-1].split(",")))
x = sum(is_triangle(the_ls))
print(x)