def get_ist_prim(n: int) -> int:
    if len(prim) >= n:
        return prim[n-1]
    num = prim[-1] + 1
    for i in range(n - len(prim)):
        while not is_prim(num):
            num += 1
        prim.append(num)
    return num

def is_prim(num):
    for i in prim:
        if num % i == 0:
            return False
    return True

prim = [2]
for _ in range(eval(input())):
    print(get_ist_prim(eval(input())) ** 2 + 1)