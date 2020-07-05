def max_time(string: str, max_letter: int, min_size: int, max_size: int) -> int:
    res = 0
    for i in range(min_size, max_size+1):
        for j in range(0, len(string)-i):
            temp = string[j:j+i]
            if len(set(temp)) > max_letter:
                continue
            else:
                count = 1
                for k in range(j+1, len(string)-i+1):
                    if string[k:k+i] == temp:
                        count += 1
                res = max(res, count)
    return res


s = input()
m_l = int(input())
min_s = int(input())
max_s = int(input())
print(max_time(s, m_l, min_s, max_s))