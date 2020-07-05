def strtoInt(s: str)-> int:
    return int(s)
def isBool(n: list, target: str) -> bool:
    tmp , t= 0, int(target)
    for i in range(len(n)-1):
        tmp = n[i]
        for j in range(1, len(n)-i):
            # i ~ i + j
            for k in range(1, j+1):
                tmp = tmp + n[i + k]
            if tmp % t == 0:
                return True
    return False
n = list(map(strtoInt, input().strip().split(",")))
target = input()
print(isBool(n, target))