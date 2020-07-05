def reduce_num(num: int) -> list:
    res = []
    if num == 1:
        return [1]
    while num != 1:
        for i in range(2, num + 1):
            if num % i == 0:
                res.append(i)
                num //= i
                break
    return res

def split_num(num: int) -> int:
    return sum(list(map(int, list(str(num)))))

for _ in range(eval(input())):
    s = eval(input())
    temp = reduce_num(s)
    print(1) if len(temp) > 1 and split_num(s) == sum([split_num(i) for i in temp]) else print(0)