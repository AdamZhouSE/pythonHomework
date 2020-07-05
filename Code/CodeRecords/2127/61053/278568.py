def mod_1337(a,lst):
    res = 1
    for no in lst:
        res = ((res**10 % 1337) * (a**no % 1337)) % 1337
    return res

if __name__ == "__main__":
    a = int(input())
    lst = list(map(int,input().split(",")))
    print(mod_1337(a,lst))