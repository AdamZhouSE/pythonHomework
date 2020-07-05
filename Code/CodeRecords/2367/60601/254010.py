def smallestRepunitDivByK(K: int) -> int:
    if K % 10 in [2, 4, 5, 6, 8]:
        return - 1
    seen = set()
    mod = 0
    for i in range(1, K + 1):
        mod = (mod * 10 + 1) % K
        if mod in seen:
            return -1
        if mod == 0:
            return i
        seen.add(mod)
print(smallestRepunitDivByK(eval(input())))