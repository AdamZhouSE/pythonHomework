from collections import defaultdict
def func(s: str, max_letter:int, min_size:int, max_size:int) -> int:

    record = defaultdict(int)
    res = 0
    for i in range(len(s) - min_size + 1):
        substring = s[i:i + min_size]
        if len(set(substring)) <= max_letter:
            record[substring] += 1
            res = max(res, record[substring])
    return res





string = input();
max_letter = int(input());
min_size = int(input());
max_size = int(input());
print(func(string, max_letter, min_size, max_size));