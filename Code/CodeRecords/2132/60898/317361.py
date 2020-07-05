import collections

def func(s: str) -> str:
    order = ["zero", "two", "four", "six", "one", "three", "five", "seven", "eight", "nine"]
    find = ["z", "w", "u", "x", "o", "r", "f", "v", "t", "e"]
    digit = [0, 2, 4, 6, 1, 3, 5, 7, 8, 9]
    record = [0 for _ in range(10)]
    dic = collections.Counter(s)
    for idx in range(10):
        cnt = dic[find[idx]]
        record[digit[idx]] += cnt
        dic = dic - collections.Counter(order[idx] * cnt)

        if not dic:
            break
    ress = ""
    for i in range(10):
        ress += str(i) * record[i]

    return ress


n = input()
print(func(n))