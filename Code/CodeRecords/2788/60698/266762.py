# 30
def test():
    n = int(input())
    ai = input().split()
    ai = list(map(int, ai))
    m = int(input())
    bj = input().split()
    bj = list(map(int, bj))
    ai.sort()
    bj.sort()
    i = 0
    count = 0
    while i < len(ai):
        for j in range(0, len(bj)):
            if match(ai[i], bj[j]):
                ai.pop(i)
                bj.pop(j)
                i = i - 1
                count = count + 1
                break
        i = i + 1
    print(count)


def match(num1: int, num2: int) -> bool:
    if abs(num1 - num2) <= 1:
        return True
    else:
        return False


test()
