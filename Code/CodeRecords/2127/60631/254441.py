def superPow(a: int, b):
    r = 1
    for _b in b:
        r = pow(r, 10, 1337) * pow(a, int(_b), 1337) % 1337
    return r
print(superPow(int(input()),input().split(',')))