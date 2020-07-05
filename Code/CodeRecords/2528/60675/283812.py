def func(mat:list) -> list:
    return sorted(mat)


n = "l = " + input()
exec(n)
print(func(l))