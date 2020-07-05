def count_par(s):
    ans_set = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s), 2):
            to_j = s[i:j]
            is_y = True
            for m in range(len(to_j) // 2):
                if to_j[m] != to_j[len(to_j) - m - 1]:
                    is_y = False
                    break
            if is_y:
                ans_set.add(to_j)
    return len(ans_set)


def not_count_par(s):
    ans_set = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            to_j = s[i:j]
            is_y = True
            if (j - i) % 2 != 1:
                is_y = False
            if is_y:
                for m in range(len(to_j) // 2):
                    if to_j[m] != to_j[len(to_j) - m - 1]:
                        is_y = False
                        break
            if not is_y:
                ans_set.add(to_j)
    return len(ans_set)


n = int(input())
st = input()
max_ab = 0
for i in range(1, n - 1):
    s = st[0:i]
    a = count_par(s)
    t = st[i:n]
    b = not_count_par(t)
    max_ab = max(max_ab, a * b)
print(max_ab)
