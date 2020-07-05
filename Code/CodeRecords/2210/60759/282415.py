ts = int(input())
for at in range(ts):
    s = input()
    t_set = set(input())
    if all(ch in s for ch in t_set):
        min_s = s
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if j - i < len(min_s) and all(ch in s[i:j] for ch in t_set):
                    min_s = s[i:j]
        print(min_s)
    else:
        print(-1)
